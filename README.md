CPU miner for fun! So that the word of 6 characters is beyond the realm of possibility.

Support only python 3.

Try call `./cpu_fun.py HI` and then you see next lines: 
```
Alphabet: eVndA6tHyLXlROs8j2157zQDZxKuP0vpqEgmMfawBrG9UJWhIT3FbNokSY4icC
W1v => HI | 4849f12249e9cee90f7acefbbb720dc03bedf4c9743cd82b52d5b1a2a6a69b62
ehn6 => HI | 48499d47a54f07a8fd83ae0823744da5d565efac4e3c12034d5003f2e9b6a4a3
ex89 => HI | 4849c2c5bbf96f579cd7f3ab7c45d31c59bdd96b38ee3bdf60d27dd933aea22f
eriL => HI | 4849479958fd57efae98b75983ba46f5bb8371fa70ed00f4a367727851c76a43
V3ln => HI | 4849b696f268a9c70daf6375cc0497f63f328746aed3ed78c2f2b184cd1f7826
VnJE => HI | 484932d97fcbaf2a10b0210cece442dc379a88ff27f00ac680d666679a595152
V1Js => HI | 4849438c450dfa63a756a294d0ead8e0b94a098f880e559f6e288c9fe03be3d3
V5FP => HI | 484970f7b659c562fbbbe9c4b067d1d1b79bffebf9bb071ded899403d14e13e7
nAmd => HI | 4849081d87a2d23463af3dd1537abd1b0cfb5d7e189f9adb4a7fdce596975a13
V9uo => HI | 48495df186bf0f4560d2586bb5737829b41c5cb0dc8442a79fc6ad8d6b5af89f
nQwa => HI | 48492f8517dfd682852702df0ac83d520a5ee4f1c6adaf665047ac5e58512f7f
nfwa => HI | 48498bd2dbf71a384aee705316c94bbec47273bd506dd576927f7204cf1f7476
nmXS => HI | 48497b78b93c033eaac7874e6cbdeab587c4bcf5ce4141578df4405aa69a20c8
nTPE => HI | 4849aee06ca678cad0d2fe015bbbe1d3075af4e100433939d9a321c0405eb76c
nIOj => HI | 4849edc12a4308c24fd2b47a4678bd8cc92d3723a19a4405c24c56fd5ca05bff
```

After that use `echo -n 'ehn6' | sha256sum` from second result.
You see the encrypted string.
Try convert it to ASCII
`echo '48499d47a54f07a8fd83ae0823744da5d565efac4e3c12034d5003f2e9b6a4a3' | xxd -r -p`
and you will get the original string.  