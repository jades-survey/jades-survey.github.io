---
layout: single
title: Data Access
permalink: /scientists/data.html
---

# JADES Data Release 3

### Temporary access to the public data products from the JWST Advanced Deep Extragalactic Survey

**These links will be live between April-May; they will be replaced by a link to the relevant MAST page, when it becomes available.**

For any information, please refer to the article by the JADES team (coming soon).
If you use these data products in your research, we would appreciate a citation to the JADES overwiev article (Eisenstein et al. 2023a), the JADES DR1 article (detailing the data reduction and spectroscopic data from PID 1210; Bunker et al. 2023b), and D'Eugenio et al. (2024). Depending on the data products used, further citations may be appropriate; Eisenstein et al. (2023b; PID 3215), Rieke et al. (2023; GOODS-S imaging) and Hainline et al. (2023; photometric redshifts).
An in-depth description of the data reduction pipeline will be provided by S. Carniani et al. (in~prep.)

### Reduced and calibrated data included in this release
1. <a href="https://www.dropbox.com/scl/fi/liea5a1dk4b0gksesotek/hlsp_jades_jwst_nirspec_clear-prism.tar.xz?rlkey=ngn9fsga14a8xxv27znwz6q4i" target="_blank">1-d and 2-d NIRSpec/MSA clear/prism spectra</a>
2. <a href="https://www.dropbox.com/scl/fi/q00fkvpsbt20u1ut4k9r1/hlsp_jades_jwst_nirspec_f070lp-g140m.tar.xz?rlkey=pejj9quyb0kxq71f3qtx79hpu" target="_blank">1-d and 2-d NIRSpec/MSA f070lp/g140m spectra</a>
3. <a href="https://www.dropbox.com/scl/fi/uxlzngots3hh3b7w96oap/hlsp_jades_jwst_nirspec_f170lp-g235m.tar.xz?rlkey=7gn7u0387gcc9evetkjbnup8v" target="_blank">1-d and 2-d NIRSpec/MSA f170lp/g235m spectra</a>
4. <a href="https://www.dropbox.com/scl/fi/9jdlvwuyqw41l4w2ba1h4/hlsp_jades_jwst_nirspec_f290lp-g395m.tar.xz?rlkey=qb0br7zz890y8gkus705mzjx9" target="_blank">1-d and 2-d NIRSpec/MSA f290lp/g395m spectra</a>

### Catalogues included in this release

0. <a href="https://www.dropbox.com/scl/fi/b69q1okxakz0wcxlu2kt2/README?rlkey=b87a7138fnxohw4b6y3mzo9bx" target="_blank">README</a>
1. <a href="https://www.dropbox.com/scl/fi/vijffz83wx9hwbhfg1503/jades_dr3_prism_public_gn_v1.1.fits?rlkey=kvhzvms1p7f617z6s2j6dj25v" target="_blank">Redshift and strong emission-line flux catalogue for prism spectra (GOODS-N)</a>
2. <a href="https://www.dropbox.com/scl/fi/ss8x24re5jr8lrh4xf7g0/jades_dr3_prism_public_gs_v1.1.fits?rlkey=3pxe5wn6jp9xqmzcz5tcfrdri" target="_blank">Redshift and strong emission-line flux catalogue for prism spectra (GOODS-S)</a>
3. <a href="https://www.dropbox.com/scl/fi/gxlitbbfyuktfcw7tf1oq/jades_dr3_medium_gratings_public_gn_v1.1.fits?rlkey=41wl0149u2et69kbok1suwujg" target="_blank">Redshift and strong emission-line flux catalogue for medium-resolution grating spectra (GOODS-N)</a>
4. <a href="https://www.dropbox.com/scl/fi/dlecaovbdzvu14zg6f8v5/jades_dr3_medium_gratings_public_gs_v1.1.fits?rlkey=7202ug7vswhpuhqo60mr4kvia" target="_blank">Redshift and strong emission-line flux catalogue for medium-resolution grating spectra (GOODS-S)</a>

### One-line terminal command to download all spectra and catalogues.

```
for f in {"https://www.dropbox.com/scl/fi/liea5a1dk4b0gksesotek/hlsp_jades_jwst_nirspec_clear-prism.tar.xz?rlkey=ngn9fsga14a8xxv27znwz6q4i\&dl=1","https://www.dropbox.com/scl/fi/q00fkvpsbt20u1ut4k9r1/hlsp_jades_jwst_nirspec_f070lp-g140m.tar.xz?rlkey=pejj9quyb0kxq71f3qtx79hpu&dl=1","https://www.dropbox.com/scl/fi/uxlzngots3hh3b7w96oap/hlsp_jades_jwst_nirspec_f170lp-g235m.tar.xz?rlkey=7gn7u0387gcc9evetkjbnup8v&dl=1","https://www.dropbox.com/scl/fi/9jdlvwuyqw41l4w2ba1h4/hlsp_jades_jwst_nirspec_f290lp-g395m.tar.xz?rlkey=qb0br7zz890y8gkus705mzjx9&dl=1","https://www.dropbox.com/scl/fi/gxlitbbfyuktfcw7tf1oq/jades_dr3_medium_gratings_public_gn_v1.1.fits?rlkey=41wl0149u2et69kbok1suwujg&dl=1","https://www.dropbox.com/scl/fi/dlecaovbdzvu14zg6f8v5/jades_dr3_medium_gratings_public_gs_v1.1.fits?rlkey=7202ug7vswhpuhqo60mr4kvia&dl=1","https://www.dropbox.com/scl/fi/vijffz83wx9hwbhfg1503/jades_dr3_prism_public_gn_v1.1.fits?rlkey=kvhzvms1p7f617z6s2j6dj25v&dl=1","https://www.dropbox.com/scl/fi/ss8x24re5jr8lrh4xf7g0/jades_dr3_prism_public_gs_v1.1.fits?rlkey=3pxe5wn6jp9xqmzcz5tcfrdri&dl=1"}; do wget $f -O $(basename "${f%%\?*}"); done
```