Problem Tickets
===============

This folder, ``docs/problem-tickets/``, is the canonical handover location for user
issues. Add a report named ``STV_PR_<NNN>.rst`` and keep screenshots/logs
beside it. Use :download:`report.rst.template <report.rst.template>` or provide
an informal text report for the problem solver to normalize. Include observed
and expected behavior, reproduction steps and environment when known.

Normalized reports contain one ``problem_report`` Need with a stable
``STV_PR_...`` ID. Status progresses from ``new`` to ``analyzed`` to ``fixed``.
Fixed reports remain in this folder. Recurrences reopen to analyzed with the
history retained. Report status is independent of requirement acceptance,
owner review and release approval. The current fixes are smoke-tested drafts
with partial verification; owner review remains pending.

.. status-pie:: problem_report

.. needtable::
   :filter: type == 'problem_report'
   :columns: id;title;status;verification_state

.. toctree::
   :glob:
   :maxdepth: 1

   STV_PR_*
