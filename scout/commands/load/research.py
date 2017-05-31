# -*- coding: utf-8 -*-
from functools import partial
import logging

import click

from scout.load.variant import delete_variants

log = logging.getLogger(__name__)


@click.command(short_help='Upload research variants')
@click.option('-c', '--case-id', help='family or case id')
@click.option('-i', '--institute', help='institute id of related cases')
@click.option('-f', '--force', is_flag=True, help='upload without request')
@click.pass_context
def research(context, case_id, institute, force):
    """Upload research variants to cases

        If a case is specified, all variants found for that case will be
        uploaded.

        If no cases are specified then all cases that have 'research_requested'
        will have there research variants uploaded
    """
    log.info("Running scout load research")
    adapter = context.obj['adapter']

    if case_id:
        if not institute:
            # Assume institute-case combo
            institute, case_id = case_id.split('-', 1)
        case_obj = adapter.case(institute_id=institute, case_id=case_id)
        if case_obj is None:
            log.info("No matching case found")
            context.abort()
        else:
            case_objs = [case_obj]
    else:
        # Fetch all cases that have requested research
        case_objs = adapter.cases(research_requested=True)

    default_threshold = 8
    for case_obj in case_objs:
        if force or case_obj.get('research_requested'):
            log.info("Delete variants for case %s", case_obj['_id'])
            delete_variants(adapter=adapter, case_obj=case_obj, variant_type='research')

            load_variants = partial(adapter.load_variants,
                                    case_obj=case_obj, variant_type='research',
                                    rank_threshold=default_threshold)

            log.info("Load research SNV for: %s", case_obj['_id'])
            load_variants(category='snv')

            if case_obj['vcf_files'].get('vcf_sv_research'):
                log.info("Load research SV for: %s", case_obj['_id'])
                load_variants(category='sv')

            adapter.case_collection.find_one_and_update(
                {'_id': case_obj['_id']},
                {'$set': {'is_research': True, 'research_requested': False}}
            )
        else:
            log.warn("research not requested, use '--force'")
