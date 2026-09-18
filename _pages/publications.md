---
layout: page
permalink: /publications/
title: Publications
description: All papers in reverse chronological order, generated from INSPIRE-HEP records.
keywords: papers preprints arXiv INSPIRE cosmology Lyman-alpha forest CMB DESI Planck
nav: true
nav_order: 2
---

{% assign cs = site.data.citation_summary %}
{% if cs %}
<p class="citation-summary">
  I have written {{ cs.papers }} papers, {{ cs.published }} of them in peer-reviewed journals. Together they have been cited
  {{ cs.citations_fmt }} times, giving an h-index of {{ cs.h_index }}
  <span class="text-muted">(INSPIRE-HEP, updated {{ cs.updated }})</span>.
</p>
{% endif %}

{% include bib_search.liquid %}

<div class="publications">

{% bibliography %}

</div>
