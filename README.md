# Implementation: On the Biometric Capacity of Generative Face Models

This repository contains the implementation of the paper "On the Biometric Capacity of Generative Face Models".

Link to paper: https://arxiv.org/abs/2308.02065

Link to official implementation repository: https://github.com/human-analysis/capacity-generative-face-models

## Download the pre-extracted features from multiple generative face models.

​ Create a folder named features and download the features.

```bash
mkdir features
```

- For ArcFace

  ```bash
  # PGAN

  mkdir features/arcface

  wget -O features/arcface/pggan_celebahq_1024.pkl https://www.dropbox.com/scl/fi/v7zr1mjixna42024tzupv/pggan_celebahq_1024.pkl?rlkey=x0yylm41c0y6xxu3hh4n7ggt5&dl=1

  # StyleGAN2-Ensemble
  wget -O features/arcface/stylegan2-ensem.pkl https://www.dropbox.com/scl/fi/96785gs6txsj0zwc62xh7/stylegan2-ensem.pkl?rlkey=b30fjn5oy4da1iyec1aamllvz&dl=1

  # StyleGAN3
  wget -O features/arcface/stylegan3.pkl https://www.dropbox.com/scl/fi/k0k76pigzbnat49ktexxf/stylegan3.pkl?rlkey=jsg4s0uxhj15jkovfaxf9mkq5&dl=1

  # Latent Diffusion
  wget -O features/arcface/ldm_celebahq_256.pkl https://www.dropbox.com/scl/fi/qmfz69zo9wiee50yh5r5g/ldm_celebahq_256.pkl?rlkey=58zb255x375k8pif8obec0kzm&dl=1

  # Generated.Photos
  wget -O features/arcface/generated.photos.pkl https://www.dropbox.com/scl/fi/7eiza4e0hxx0rdzewgrbo/generated.photos.pkl?rlkey=lrvik48cjvihnu6k2nr54cxhw&dl=1

  # DCFace
  wget -O features/arcface/dcface_0.5m.pkl https://www.dropbox.com/scl/fi/twe5yjyj5r0zcahg9cy6y/dcface_0.5m.pkl?rlkey=awl795v2lzhorf2qhxdtroxar&dl=1
  ```

- For AdaFace

  ```bash
  # PGGAN

  mkdir features/adaface

  wget -O features/adaface/pggan_celebahq_1024.pkl https://www.dropbox.com/scl/fi/x2nrg2stu6w7dckyed400/pggan_celebahq_1024.pkl?rlkey=xanxngi06jt7rqhjqks10r73x&dl=1

  # StyleGAN2-Ensemble
  wget -O features/adaface/stylegan2-ensem.pkl https://www.dropbox.com/scl/fi/7gva422lcp2wduzv079ma/stylegan2-ensem.pkl?rlkey=psgzw3hkv2e7fneo82pp69g98&dl=1

  # StyleGAN3
  wget -O features/adaface/stylegan3.pkl https://www.dropbox.com/scl/fi/9mz8vtnm18d2suzkvudtb/stylegan3.pkl?rlkey=clmnl035o4e24cwa1y1et4trw&dl=1

  # Latent Diffusion
  wget -O features/adaface/ldm_celebahq_256.pkl https://www.dropbox.com/scl/fi/g0sj9x0y7ciwky5zg1tln/ldm_celebahq_256.pkl?rlkey=j42npo4godbm7b61h2umcwkcl&dl=1

  # Generated.Photos
  wget -O features/adaface/generated.photos.pkl https://www.dropbox.com/scl/fi/nkk4zk74n2th97xnc1gbd/generated.photos.pkl?rlkey=8veot2a9gia79eo6vuakbu5s9&dl=1

  # DCFace
  wget -O features/adaface/dcface_0.5m.pkl https://www.dropbox.com/scl/fi/dgkajfrqxbvtad355fqwj/dcface_0.5m.pkl?rlkey=gwcsr4u221d8zgkwk5tcwxs23&dl=1
  ```
