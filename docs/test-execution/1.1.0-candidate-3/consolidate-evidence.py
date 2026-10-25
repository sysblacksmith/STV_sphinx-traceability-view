"""Consolidate actual completed reports; never turn failed suites into passes."""
from collections import defaultdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
result=json.loads((HERE/'results.json').read_text(encoding='utf-8'))
# Retain the failed full attempt as failed; a later candidate supplies retests.
previous=json.loads((HERE.parent/'1.1.0-candidate-2/case-results.json').read_text(encoding='utf-8'))
known=defaultdict(set)
for item in previous:
    if item['report'] in ['pytest.xml','node.xml']:known[item['selector']].add(item['case_id'])
extra={
 'test_reset_stale_layout_failure_retry_and_independent_views':['STV_TC_SY_066'],
 'test_reset_overview_boundaries_and_page_restoration_cache':['STV_TC_SY_066'],
 'test_reset_uses_interactive_seed_and_retains_hidden_artifact_card':['STV_TC_SY_066'],
 'test_extended_reset_command_sequences':['STV_TC_SW_051'],
 'test_typography_nested_units_late_children_and_repeat_scaling':['STV_TC_SW_052'],
 'test_font_defaults_legacy_fallback_reuse_resize_and_host_isolation':['STV_TC_SY_068'],
 'test_font_settings_defaults_identity_and_named_build_errors':['STV_TC_SW_052'],
 'test_download_expiry_pagehide_and_error_ownership':['STV_TC_SW_053'],
 'test_snapshot_clipping_immutable_text_resources_and_readiness':['STV_TC_SW_053'],
 'test_export_pointer_snapshot_cancel_keyboard_and_serialization_recovery':['STV_TC_SW_053'],
 'test_export_resource_retry_and_pending_fonts_refuse_capture':['STV_TC_SW_053','STV_TC_SW_055'],
 'test_real_font_and_selected_local_media_are_self_contained':['STV_TC_SW_053','STV_TC_SW_055'],
 'test_host_bulk_mixed_rows_reinitialization_and_native_toggle':['STV_TC_SY_069','STV_TC_SW_054'],
 'test_page_metadata_excludes_copies_and_handles_empty_pages':['STV_TC_SW_054'],
}
groups=defaultdict(list);unmapped=[];rows=[]
for case in result['cases']:
    selector=case['test'];name=selector.split('::')[-1].split('[')[0]
    ids=known.get(selector,set()) or set(extra.get(name,[]))
    if not ids and 'test_extended_export_resources' in selector:ids={'STV_TC_SW_055'}
    if not ids:
        unmapped.append(case);continue
    for identity in ids:
        row={'selector':selector,'case_id':identity,'result':case['outcome'],
             'report':'node.xml' if selector.startswith('test::') else 'pytest.xml',
             'report_completed_at':result['finished'],'mapping_source':'Candidate-2 canonical mapping plus reviewed extended criterion allocation'}
        groups[identity].append(row);rows.append(row)
assert len(unmapped)==7, 'Review newly unmapped executable cases: '+str(unmapped)
lines=['Canonical candidate-3 executions','=================================','',
       'These are actual full-selection observations at the committed extended test',
       'baseline. Manual observations and unchanged capacity supplements are linked',
       'separately in :doc:`extended-qualification`; they are not invented fresh tests.','']
for identity,items in sorted(groups.items()):
    execution='STV_TE_'+hashlib.sha256((HERE.name+identity).encode()).hexdigest()[:16].upper()
    outcome='failed' if any(i['result']!='passed' for i in items) else 'passed'
    for item in items:item['execution_id']=execution
    evidence='; '.join('docs/test-execution/'+HERE.name+'/'+p for p in sorted({i['report'] for i in items}))
    lines += [f'.. test_execution:: {identity} candidate-3 variants',f'   :id: {execution}',
      '   :status: recorded','   :basis: observed',f'   :evidence: {evidence}','   :priority: unassigned',
      '   :verification_state: not_assessed',f'   :result: {outcome}',f'   :executed_at: {result["finished"]}','',
      f'   :need:`{identity}`: {len(items)} actual automated variants; aggregate {outcome}.',
      '   Full selectors, candidate identity and outcomes are retained in',
      '   :download:`case-results.json <case-results.json>` and :doc:`index`.','']
    path=ROOT/'docs/test-cases'/('system-tests.rst' if '_SY_' in identity else 'software-tests.rst')
    text=path.read_text(encoding='utf-8')
    pattern=r'(:id: '+identity+r'\n)(.*?)(?=\n\.\. test_case::|\Z)'
    match=re.search(pattern,text,re.S);assert match,identity
    block=match.group(0)
    if execution not in block:
        block=re.sub(r'(:executed_by: [^\n]+)',r'\g<1>, '+execution,block)
    block=re.sub(r':last_result: \w+',':last_result: '+outcome,block)
    text=text[:match.start()]+block+text[match.end():];path.write_text(text,encoding='utf-8')
(HERE/'cases.rst').write_text('\n'.join(lines),encoding='utf-8')
(HERE/'case-results.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
(HERE/'infrastructure-results.json').write_text(json.dumps(unmapped,indent=2)+'\n',encoding='utf-8')
baseline=result['revision'];compared={}
for name,recorded_hash in json.loads((HERE/'source-hashes.json').read_text(encoding='utf-8')).items():
    committed=subprocess.check_output(['git','show',baseline+':'+name],cwd=ROOT)
    variants=[committed]
    if b'\x00' not in committed:
        lf=committed.replace(b'\r\n',b'\n');variants.extend([lf,lf.replace(b'\n',b'\r\n')])
    normalized=recorded_hash in {hashlib.sha256(value).hexdigest() for value in variants}
    current=(ROOT/name).read_bytes()
    if hashlib.sha256(current).hexdigest()==recorded_hash:
        normalized=normalized or current.replace(b'\r\n',b'\n')==committed.replace(b'\r\n',b'\n')
    assert normalized,name
    compared[name]={'recorded_sha256':recorded_hash,'matches_committed_content':normalized}
(HERE/'test-baseline.json').write_text(json.dumps({'revision':baseline,'recorded_at':datetime.now(timezone.utc).isoformat(),
    'comparison':'Git text line endings normalized; runtime bytes are checked separately by publication validation','files':compared},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'canonical_cases':len(groups),'mapped_variants':len(rows),'infrastructure_cases':len(unmapped),'baseline':baseline},indent=2))
