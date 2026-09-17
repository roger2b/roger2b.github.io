---
layout: page
permalink: /research/
title: Research
description: An overview of my main research directions and key results, organised by theme.
keywords: Lyman-alpha forest effective field theory field-level inference bispectrum BAO DESI CMB lensing quasars neutrino mass reionization B-modes foregrounds axions machine learning hydrodynamic simulations
nav: true
nav_order: 1
---

*A guided tour of my research. The complete list of papers is on the [publications page]({{ '/publications/' | relative_url }}) and on [INSPIRE](https://inspirehep.net/authors/1720237).*

## The Lyman-α forest

### Modelling the forest at the field level

<img class="research-fig" src="{{ '/assets/img/research/b_field_level_lya.png' | relative_url }}" alt="Field-level model of the Lyman-alpha forest compared with a hydrodynamic simulation">

The Lyman-α forest is the pattern of absorption that hydrogen gas leaves in the light of distant quasars. It maps the cosmic web when the Universe was about a fifth of its present age. I developed the first analytic model that predicts this pattern directly from the initial conditions of the Universe, rather than only its statistical summaries. Compared with detailed hydrodynamic simulations, the model reproduces the forest to within a few per cent down to scales of a few megaparsecs, and a hybrid version that borrows particle motions from large simulations reaches even smaller scales. This work, highlighted in *Physics*, underpins the theory effort of the DESI Lyman-α analysis and now extends to the forest's cross-correlation with distant galaxies.

Key papers: [de Belsunce, Ivanov, Sullivan, Akitsu & Chen 2026, PRL](https://arxiv.org/abs/2507.00284) · [de Belsunce, Hadzhiyska & Ivanov 2026, PRD](https://arxiv.org/abs/2512.13681) · [de Belsunce, Ivanov, Sullivan, Chen & Akitsu 2026](https://arxiv.org/abs/2606.26234)

<div style="clear: both;"></div>

### The three-dimensional power spectrum

<img class="research-fig" src="{{ '/assets/img/research/g_lya_p3d.png' | relative_url }}" alt="Three-dimensional power spectrum of the Lyman-alpha forest measured from eBOSS">

Until recently the forest was analysed mostly along individual lines of sight. Using about 205,000 quasar spectra from the eBOSS survey, we made the first measurement of its full three-dimensional power spectrum, the statistic that captures how the absorption is correlated across the sky as well as along the line of sight. With Benjamin Horowitz and Zarija Lukić I also developed MAPLE, a code that estimates this spectrum and its uncertainties for surveys with sparse sightlines.

Key papers: [de Belsunce, Philcox, Iršič et al. 2024, MNRAS](https://arxiv.org/abs/2403.08241) · [Horowitz, de Belsunce & Lukić 2024, MNRAS](https://arxiv.org/abs/2403.17294)

<div style="clear: both;"></div>

### Beyond two-point statistics: the compressed bispectrum

<img class="research-fig" src="{{ '/assets/img/research/c_lya_bispectrum.png' | relative_url }}" alt="Skew spectra of the Lyman-alpha forest compared with theory">

Two-point statistics discard information about the shape of the cosmic web. We extended a compact form of the three-point function, the skew spectra, to the forest and derived its prediction within the theoretical framework used by DESI. A new variant that shifts the field along the line of sight makes the method directly applicable to survey data.

Key papers: [de Belsunce, Sullivan & McDonald 2026, PRD](https://arxiv.org/abs/2510.23597)

<div style="clear: both;"></div>

### A standard ruler in the forest

<img class="research-fig" src="{{ '/assets/img/research/e_lya_bao_shift.png' | relative_url }}" alt="Shift of the baryon acoustic oscillation peak in the Lyman-alpha forest">

The forest measures the baryon acoustic oscillation scale, a standard ruler for the expansion history of the Universe. We showed that nonlinear evolution shifts this ruler by a few tenths of a per cent, which matters at DESI's precision, and provided the error budget and priors that account for it. With Boryana Hadzhiyska we then measured the shift directly in large mock catalogues and showed that the theoretical model recovers the ruler without bias.

Key papers: [de Belsunce, Chen, Ivanov et al. 2025, PRD](https://arxiv.org/abs/2412.06892) · [Hadzhiyska, de Belsunce et al. 2025, MNRAS](https://arxiv.org/abs/2503.13442)

<div style="clear: both;"></div>

### Simulations enhanced with deep learning

<img class="research-fig" src="{{ '/assets/img/research/f_deep_learning_hydro.png' | relative_url }}" alt="Low-resolution simulation slice enhanced with a deep-learning model">

Simulating the forest over survey-sized volumes at the required resolution is beyond current computers. With Cooper Jacobus, a student I supervised at Berkeley, we trained a generative deep-learning model on a small high-resolution simulation and used it to enhance a low-resolution volume nearly a gigaparsec across, reproducing the small-scale statistics of the forest to within about ten per cent.

Key papers: [Jacobus, de Belsunce et al. 2025, ApJ](https://arxiv.org/abs/2411.16920)

<div style="clear: both;"></div>

## Neutrinos, growth of structure and cross-correlations

### A tentative detection of neutrino mass

<img class="research-fig" src="{{ '/assets/img/research/a_neutrino_mass.png' | relative_url }}" alt="Constraints on the sum of neutrino masses">

Cosmology can weigh neutrinos, but today's data sets disagree mildly with one another within the standard model. With James Sullivan and Mikhail Ivanov we showed that a single change, a higher optical depth to reionization, removes the tension in the Hubble constant, the preference for negative neutrino masses and the hints of evolving dark energy all at once. In this picture we obtain a first tentative detection of a positive neutrino mass, about a tenth of an electron-volt.

Key papers: [Sullivan, de Belsunce & Ivanov 2026](https://arxiv.org/abs/2606.30903)

<div style="clear: both;"></div>

### Lensing of the microwave background by quasars

<img class="research-fig" src="{{ '/assets/img/research/d_lensing_quasars.png' | relative_url }}" alt="Cross-correlation of Planck CMB lensing with DESI quasars">

Gravitational lensing of the cosmic microwave background traces all the matter along the line of sight. I led the cross-correlation of the Planck lensing map with 1.2 million DESI quasars in three redshift slices, detected at more than twenty sigma, which measures how fast structure grew when the Universe was two to six billion years old. Combined with lensing data we also obtained a measurement of the Hubble constant that does not rely on the sound-horizon scale.

Key papers: [de Belsunce et al. 2025, JCAP](https://arxiv.org/abs/2506.22416)

<div style="clear: both;"></div>

### Massive neutrinos in the clustering of matter

<img class="research-fig" src="{{ '/assets/img/research/l_eft_neutrinos.png' | relative_url }}" alt="Tree-level bispectrum of matter with massive neutrinos">

Neutrinos have mass and move fast, which subtly changes how matter clusters. With Leonardo Senatore I computed the three-point clustering of matter including massive neutrinos within the effective field theory of large-scale structure, and found that neutrinos enhance the signal on small scales by about sixteen times their mass fraction.

Key papers: [de Belsunce & Senatore 2019, JCAP](https://arxiv.org/abs/1804.06849)

<div style="clear: both;"></div>

## The polarized microwave sky with Planck

### When the first stars lit up

<img class="research-fig" src="{{ '/assets/img/research/k_optical_depth.png' | relative_url }}" alt="Constraints on the optical depth to reionization from Planck">

The polarization of the cosmic microwave background on the largest angular scales records when the first stars reionized the Universe. We developed three complementary statistical methods for these noisy, partial-sky Planck maps and obtained an optical depth to reionization of about 0.063, one of the most precise determinations from Planck.

Key papers: [de Belsunce, Gratton, Coulton & Efstathiou 2021, MNRAS](https://arxiv.org/abs/2103.14378)

<div style="clear: both;"></div>

### Searching for primordial gravitational waves

<img class="research-fig" src="{{ '/assets/img/research/h_planck_bmodes.png' | relative_url }}" alt="Constraints on the tensor-to-scalar ratio from Planck polarization">

Gravitational waves from the first instants of the Universe would leave a faint curl-like pattern, called B modes, in the polarization of the microwave background. After cleaning the Galactic foregrounds with a Bayesian method, we used the large-scale Planck polarization data alone to limit the amplitude of such waves to less than about a quarter of the density fluctuations.

Key papers: [de Belsunce, Gratton & Efstathiou 2022, MNRAS](https://arxiv.org/abs/2207.04903)

<div style="clear: both;"></div>

### Seeing through the Galaxy

<img class="research-fig" src="{{ '/assets/img/research/j_foreground_index.png' | relative_url }}" alt="Spatial variation of the synchrotron spectral index across the sky">

Polarized emission from our own Galaxy is the main obstacle to measuring the primordial signal. We built a Bayesian method that separates the microwave background from synchrotron and dust emission while letting their spectral properties vary across the sky. We found evidence that the synchrotron spectrum does vary, while dust behaves uniformly.

Key papers: [de Belsunce, Gratton & Efstathiou 2022, MNRAS](https://arxiv.org/abs/2205.13968)

<div style="clear: both;"></div>

### Axions and the rotation of light

<img class="research-fig" src="{{ '/assets/img/research/i_axion_birefringence.png' | relative_url }}" alt="Cosmic birefringence from recombination and reionization">

If axion-like particles exist, they rotate the polarization of light travelling through them, an effect known as cosmic birefringence. With Patricia Diego-Palazuelos we showed how to separate the rotation of light emitted when the Universe first became transparent from that of light emitted during reionization, turning the microwave background into a probe of how such a field evolved over cosmic time.

Key papers: [Diego-Palazuelos, de Belsunce, Gratton & Sherwin 2024, PoS](https://doi.org/10.22323/1.454.0047)

<div style="clear: both;"></div>
