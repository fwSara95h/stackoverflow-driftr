---
title: "Why when extracting products data shows me that they are duplicate?"
site: stackoverflow
question_id: 75073129
answer_id: 75074352
url: https://stackoverflow.com/a/75074352
author: "Sergey K"
author_url: https://stackoverflow.com/users/6593287
posted: 2023-01-10T18:29:53Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e78a8bb183a72162e84a3a9c3a6c23a346c0c857787029396100c7d8020048aa
role: another answer on the same question, kept as context; not my work
---

# Answer by [Sergey K](https://stackoverflow.com/users/6593287) — 2023-01-10

Posted on Stack Overflow, <https://stackoverflow.com/a/75074352>, 2023-01-10. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You can simple use api on this site

    import requests
    import pandas as pd
    
    
    result = []
    
    for page in range(1, 3):
        url = f"https://api.niceonesa.com/?route=rest/product_admin/products&seo_url=appcomponent--best-sales&page={page}&sort=most_popular&limit=60&first=false"
        headers = {
            'authority': 'api.niceonesa.com',
            'accept': 'application/json, text/plain, */*',
            'content-type': 'application/json',
            'platform': 'web',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        }
        response = requests.get(url, headers=headers)
        for product in response.json()['data']['products']:
            result.append({
                'link': product['share_url'],
                'title': product['en_name'],
                'brand': product['manufacturer'],
                'price': product['price_formated'],
                'offer': product['price'],
                'rate': product['total_reviews'],
                'rate_starts': product['rating'],
            })
    
    df = pd.DataFrame(result)

DF OUTPUT:

                                                                                                                                     link                                                                            title                brand         price   offer  rate  rate_starts
    0                                           https://niceonesa.com/ar/gifts/travel-size/ola-hair-mini-straightener-brush-n-215-n16250/                                         Ola Hair Mini Straightener Brush - N-215             Ola Hair  160.43 ريال   128.34  1730          4.9
    1        https://niceonesa.com/ar/care/face-care/face-moisturizer/bodyblendz-vitamin-c-hyaluronic-acid-penetrating-serum-30ml-n18420/                    BodyBlendz Vitamin C Hyaluronic Acid Penetrating Serum - 30ml          Body Blendz      65 ريال    65.00   243          5.0
    2                           https://niceonesa.com/ar/makeup/eyes/mascara/essence-lash-princess-false-lash-effect-mascara-black-n6722/                          Essence Lash Princess False Lash Effect Mascara - Black              essence   25.30 ريال    18.40  3272          5.0
    3      https://niceonesa.com/ar/care/face-care/tools-and-accessories/feather-flamingo-s-for-shaving-facial-body-hair-3-pieces-n12850/                       Feather-Flamingo S For Shaving Facial Body Hair - 3 Pieces     Feather-Flamingo   17.53 ريال    13.00  1252          5.0
    4                                https://niceonesa.com/ar/makeup/eyes/mascara/essence-i-love-extreme-crazy-volume-mascara-black-n452/                              Essence I Love Extreme Crazy Volume Mascara - Black              essence   20.70 ريال    18.00  2979          4.9
    5                              https://niceonesa.com/ar/makeup/lips/liquid-lipstick/etude-house-dear-darling-water-tint-cherry-n2826/                                     Etude House Dear Darling Water Tint - Cherry          Etude House   30.67 ريال    17.83  2163          4.9
    6                                            https://niceonesa.com/ar/makeup/eyes/eyeliner/thebalm-schwing-liquid-eyeliner-black-n34/                                          theBalm Schwing Liquid Eyeliner - Black    theBalm Cosmetics   63.25 ريال    29.00  2613          4.9
    7                                  https://niceonesa.com/ar/makeup/eyes/mascara/bourjois-twist-up-the-volume-mascara-ultra-black-n67/                               Bourjois Twist Up The Volume Mascara - Ultra Black             Bourjois   44.85 ريال    33.00  2868          4.9
    8                              https://niceonesa.com/ar/makeup/eyes/eyeliner/rimmel-london-scandaleyes-waterproof-eyeliner-nude-n320/                             Rimmel London Scandaleyes Waterproof Eyeliner - Nude        Rimmel London   32.20 ريال    19.55  1797          5.0
    9                                    https://niceonesa.com/ar/makeup/eyes/eyeliner/mahmood-saeed-elizabeth-helen-eyeliner-black-n503/                                   Mahmood Saeed Elizabeth Helen Eyeliner - Black        Mahmood Saeed   19.55 ريال    18.96  1192          5.0
    10                                   https://niceonesa.com/ar/makeup/eyebrow/eyebrow-mascara/essence-lash-and-brow-gel-mascara-n1561/                                                Essence Lash and Brow Gel Mascara              essence   32.20 ريال    16.10  1384          4.9
    11  https://niceonesa.com/ar/makeup/face/makeup-removers/garnier-skin-active-micellar-cleansing-water-for-sensitive-skin-400ml-n3378/          Garnier Skin Active Micellar Cleansing Water For Sensitive Skin - 400ml              Garnier      29 ريال    25.05   951          5.0
    12                            https://niceonesa.com/ar/makeup/face/makeup-spray/topface-fix-quickly-makeup-setting-spray-100ml-n8394/                                 Topface Fix Quickly Makeup Setting Spray - 100ml              Topface   35.02 ريال    35.02   763          4.9
    13                                       https://niceonesa.com/ar/makeup/face/face-primer/maybelline-baby-skin-instant-pore-22ml-n44/                                         Maybelline Baby Skin Instant Pore - 22ml           Maybelline   51.75 ريال    37.38  1406          4.9
    14                                       https://niceonesa.com/ar/makeup/brushes-amp-tools/face-brushes/marble-angled-brush-m1-n5596/                                                         Marble Angled Brush - M1               MARBLE   65.71 ريال    59.34   941          4.9
    15                                         https://niceonesa.com/ar/care/face-care/tools-and-accessories/derma-roller-4-in-1-kit-n80/                                                          Derma roller 4 in 1 Kit  Derma roller System  149.50 ريال    36.80  1000          4.9
    16                                    https://niceonesa.com/ar/makeup/face/bb-amp-cc-cream/missha-m-perfect-cover-bb-cream-no-27-n69/                                          Missha M Perfect Cover BB Cream - No.27               Missha   79.35 ريال    44.85  1158          4.9
    17                                     https://niceonesa.com/ar/makeup/eyes/eyeshadow/revolution-reloaded-palette-iconic-fever-n9234/                                       Revolution Reloaded Palette - Iconic Fever           Revolution      65 ريال    42.25  1158          5.0
    18                                     https://niceonesa.com/ar/care/face-care/lip-care/carmex-classic-lip-balm-medicated-10g-n13459/                                          Carmex Classic Lip Balm Medicated - 10g               Carmex   19.55 ريال    15.64   698          5.0
    19                                             https://niceonesa.com/ar/makeup/lips/lip-liner/topface-waterproof-lipliner-110-n17038/                                               Topface Waterproof Lipliner - 110               Topface      25 ريال    25.00   120          4.9
    20                        https://niceonesa.com/ar/care/hair-care/oil-amp-masks/nature-repeat-aloe-vera-92-soothing-gel-300ml-n11782/                                 Nature Repeat Aloe Vera 92% Soothing Gel - 300ml        Nature Repeat      20 ريال    18.00   741          4.9
    21                                https://niceonesa.com/ar/care/face-care/eye-care/the-ordinary-caffeine-solution-5-egcg-30ml-n11906/                                  The Ordinary Caffeine Solution 5% + EGCG - 30ml         The Ordinary   66.81 ريال    60.95   448          4.9
    22                                       https://niceonesa.com/ar/gifts/men-gift-sets/blanco-musk-set-eau-de-perfume-4-pieces-n15556/                                      Blanco Musk Set - Eau De Perfume - 4 Pieces               BLANCO  366.85 ريال   199.00   705          4.9
    23                               https://niceonesa.com/ar/makeup/eyes/eyeliner/jockey-eyeliner-unique-and-soft-intensive-black-n5512/                                Jockey Eyeliner Unique and Soft - Intensive Black              Jockey    21.85 ريال    18.40   744          5.0
    24                                         https://niceonesa.com/ar/devices/hair-devices/jose-eber-pro-series-curling-iron-25mm-n522/                                         Jose Eber Pro Series curling iron - 25mm            jose eber     253 ريال   127.01   742          4.9
    25             https://niceonesa.com/ar/care/face-care/tools-and-accessories/derma-roller-system-derma-roller-for-skin-0-50mm-n11109/                               Derma Roller System Derma Roller for skin - 0.50mm  Derma roller System   31.76 ريال    24.46   131          4.9
    26                         https://niceonesa.com/ar/makeup/lips/liquid-lipstick/etude-house-dear-darling-water-tint-strawberry-n2824/                                 Etude House Dear Darling Water Tint - Strawberry          Etude House      31 ريال    16.50   334          4.9
    27               https://niceonesa.com/ar/makeup/highlighter/powder-highlighter/revolution-ultra-blush-palette-sugar-and-spice-n7846/                                 Revolution Ultra Blush Palette - Sugar and Spice           Revolution      96 ريال    62.40   768          5.0
    28                                             https://niceonesa.com/ar/makeup/eyes/mascara/topface-focus-point-volume-mascara-n8341/                                               Topface Focus Point Volume Mascara              Topface   30.19 ريال    28.00   485          5.0
    29                                 https://niceonesa.com/ar/makeup/face/powder/topface-instyle-loose-powder-banana-smart-shade-n8356/                                Topface Instyle Loose Powder - Banana Smart Shade              Topface   71.30 ريال    58.00   925          5.0
    30                                    https://niceonesa.com/ar/devices/hair-devices/jose-eber-wet-or-dry-styling-iron-1-5-inch-n7910/                                     Jose Eber Wet Or Dry Styling Iron - 1.5 inch            jose eber  228.85 ريال   128.00   152          4.9
    31                                           https://niceonesa.com/ar/devices/hair-devices/okema-1200-shift-hair-styler-ok2118-n3732/                                            Okema 1200 Shift Hair Styler - OK2118                Okema  171.35 ريال   154.10   431          4.9
    32                                  https://niceonesa.com/ar/makeup/face/foundation/m-asam-magic-finish-makeup-foundation-30ml-n8181/                                    M. Asam Magic Finish Makeup Foundation - 30ml              M. Asam  126.50 ريال   120.18   547          4.7
    33        https://niceonesa.com/ar/makeup/lips/lip-sets/thebalm-meet-matte-hughes-set-of-6-mini-lipsticks-limited-edition-vol2-n1750/         theBalm Meet Matte Hughes Set of 6 Mini Lipsticks Limited Edition - Vol2    theBalm Cosmetics  148.35 ريال    75.00  1303          4.9
    34                                          https://niceonesa.com/ar/makeup/highlighter/palette-amp-set/ofra-pro-palette-soul-n11717/                                                          OFRA Pro Palette - Soul                OFRA   262.86 ريال   227.00   232          4.9
    35                                                   https://niceonesa.com/ar/devices/hair-devices/okema-4000-hair-dryer-ok882-n3723/                                                    Okema 4000 Hair Dryer - OK882                Okema  212.75 ريال   172.50    93          5.0
    36                                          https://niceonesa.com/ar/nails/nails-polish/topface-lasting-color-nail-enamel-053-n10050/                                          Topface Lasting Color Nail Enamel - 053              Topface   18.40 ريال     5.50    37          4.9
    37                                         https://niceonesa.com/ar/devices/hair-devices/jose-eber-pro-series-curling-iron-19mm-n258/                                         Jose Eber Pro Series Curling Iron - 19mm            jose eber     253 ريال   127.01   263          4.9
    38                                                       https://niceonesa.com/ar/devices/hair-devices/okema-hair-styler-ok977-n2928/                                                        Okema Hair Styler - OK977                Okema  136.85 ريال   113.85    45          4.6
    39                                               https://niceonesa.com/ar/perfume/musk/blanco-musk-special-eau-de-perfum-50ml-n16233/                                         Blanco Musk Special- Eau de Perfum- 50ml               BLANCO     147 ريال    75.00   104          4.9
    40                            https://niceonesa.com/ar/makeup/brushes-amp-tools/sponges-amp-tools/ksd-puff-facial-powder-sponge-n330/                                                    KSD Puff Facial Powder Sponge                  KSD   32.20 ريال    20.70   454          4.9
    41                                 https://niceonesa.com/ar/perfume/home-scents/oud-amp-bakhoor/nice-one-morouke-mini-1-ounce-n15086/                                                  Nice One Morouke Mini - 1 Ounce              Niceone  172.50 ريال   117.00   464          4.9
    42                                           https://niceonesa.com/ar/nails/nails-polish/topface-lasting-color-nail-enamel-079-n8401/                                          Topface Lasting Color Nail Enamel - 079              Topface   18.40 ريال    15.00   135          4.9
    43                                          https://niceonesa.com/ar/nails/nails-polish/topface-lasting-color-nail-enamel-020-n10047/                                          Topface Lasting Color Nail Enamel - 020              Topface   18.40 ريال    15.00   123          4.9
    44                                                https://niceonesa.com/ar/devices/hair-devices/okema-shift-hair-styler-ok2113-n3713/                                                 Okema Shift Hair Styler - OK2113                Okema  132.25 ريال   121.33    68          4.8
    45                https://niceonesa.com/ar/makeup/brushes-amp-tools/brush-sets/bh-cosmetics-pink-perfection-brush-set-10-piece-n3161/                               BH Cosmetics Pink Perfection Brush Set - 10 Piece          BH cosmetics  102.35 ريال    68.00   373          4.9
    46                                https://niceonesa.com/ar/devices/hair-devices/jose-eber-100-ceramic-flat-iron-1-25-inch-pink-n1508/                              Jose Eber 100% Ceramic Flat Iron - 1.25 Inch - Pink            jose eber  287.50 ريال   179.00   312          4.9
    47                                           https://niceonesa.com/ar/nails/nails-polish/topface-lasting-color-nail-enamel-002-n8406/                                          Topface Lasting Color Nail Enamel - 002              Topface   18.40 ريال    15.00   139          4.9
    48                                          https://niceonesa.com/ar/devices/hair-devices/jose-eber-clipless-curling-iron-32mm-n3286/                                           Jose Eber Clipless Curling Iron - 32mm            jose eber     253 ريال   156.98    80          4.9
    49                                           https://niceonesa.com/ar/nails/nails-polish/topface-lasting-color-nail-enamel-061-n8396/                                          Topface Lasting Color Nail Enamel - 061              Topface   18.40 ريال    15.00   138          5.0
    50                                          https://niceonesa.com/ar/nails/nails-polish/topface-lasting-color-nail-enamel-024-n10045/                                          Topface Lasting Color Nail Enamel - 024              Topface   18.40 ريال    15.00   164          5.0
    51                                                 https://niceonesa.com/ar/makeup/lips/lipstick/mood-matcher-lipstick-yellow-n16681/                                                   Mood Matcher Lipstick - Yellow         Mood Matcher   40.94 ريال    40.94    59          5.0
    52                                           https://niceonesa.com/ar/nails/nails-polish/topface-lasting-color-nail-enamel-047-n8384/                                          Topface Lasting Color Nail Enamel - 047              Topface   18.40 ريال    15.00    63          4.9
    53                                          https://niceonesa.com/ar/nails/nails-polish/topface-lasting-color-nail-enamel-040-n10035/                                          Topface Lasting Color Nail Enamel - 040              Topface   18.40 ريال    15.00   114          5.0
    54                                           https://niceonesa.com/ar/nails/nails-polish/topface-lasting-color-nail-enamel-037-n8347/                                          Topface Lasting Color Nail Enamel - 037              Topface   18.40 ريال    15.00    96          5.0
    55                                     https://niceonesa.com/ar/perfume/oud-perfume/blanco-royal-dehn-oud-mukhallat-half-tola-n15900/                                      Blanco Royal Dehn Oud mukhallat - Half Tola               BLANCO     294 ريال   151.00    92          5.0
    56                                           https://niceonesa.com/ar/nails/nails-polish/topface-lasting-color-nail-enamel-010-n8400/                                          Topface Lasting Color Nail Enamel - 010              Topface   18.40 ريال    15.00   243          5.0
    57                                           https://niceonesa.com/ar/nails/nails-polish/topface-lasting-color-nail-enamel-018-n8547/                                          Topface Lasting Color Nail Enamel - 018              Topface   18.40 ريال    15.00    66          5.0
    58                                                  https://niceonesa.com/ar/devices/hair-devices/okema-4000-hair-dryer-ok1070-n3716/                                                   Okema 4000 Hair Dryer - OK1070                Okema  218.50 ريال   177.10    56          4.8
    59                                           https://niceonesa.com/ar/nails/nails-polish/topface-lasting-color-nail-enamel-045-n8383/                                          Topface Lasting Color Nail Enamel - 045              Topface   18.40 ريال    15.00    81          4.9
    60                           https://niceonesa.com/ar/devices/hair-devices/jose-eber-clipless-curling-iron-13mm-pink-amp-black-n7466/                            Jose Eber Clipless Curling Iron - 13mm - Pink & Black            jose eber  217.35 ريال   172.50    19          4.5
    61                          https://niceonesa.com/ar/nails/nails-care/kinetics-nano-shark-green-efficient-nail-treatment-15ml-n16122/                        Kinetics Nano Shark Green Efficient Nail Treatment - 15ml             kinetics   80.50 ريال    32.99    55          4.8
    62                                   https://niceonesa.com/ar/perfume/perfume-offers/guerlain-santal-royal-125ml-eau-de-parfum-n1522/                                    Guerlain Santal Royal - 125ml - Eau De Parfum             Guerlain  688.85 ريال   688.85   240          4.9
    63                                  https://niceonesa.com/ar/care/face-care/tools-and-accessories/gemstone-facial-roller-pink-n16252/                                                    Gemstone Facial Roller - Pink              Niceone   92.98 ريال    42.00    61          5.0
    64                                           https://niceonesa.com/ar/nails/nails-polish/topface-lasting-color-nail-enamel-034-n8376/                                          Topface Lasting Color Nail Enamel - 034              Topface   18.40 ريال    15.00   108          5.0
    65                               https://niceonesa.com/ar/care/hair-care/oil-amp-masks/now-solutions-liquid-coconut-oil-118ml-n13158/                                         Now Solutions Liquid Coconut Oil - 118ml                 now    56.95 ريال    39.00    25          4.8
    66                                      https://niceonesa.com/ar/devices/facial-devices/sonata-9-in-1-electric-beauty-clean-set-n382/                                          Sonata 9 in 1 Electric Beauty Clean Set              Sonata      138 ريال   110.40    22          4.5
    67                                           https://niceonesa.com/ar/nails/nails-polish/topface-lasting-color-nail-enamel-014-n8552/                                          Topface Lasting Color Nail Enamel - 014              Topface   18.40 ريال    15.00   143          5.0
    68                                     https://niceonesa.com/ar/care/face-care/tools-and-accessories/5in1-derma-roller-system-n15441/                                                        5In1 Derma Roller System   Derma roller System      69 ريال    62.10     2          5.0
    69                                          https://niceonesa.com/ar/nails/nails-polish/topface-lasting-color-nail-enamel-057-n10042/                                          Topface Lasting Color Nail Enamel - 057              Topface   18.40 ريال    15.00    45          4.9
    70                                   https://niceonesa.com/ar/devices/hair-devices/joy-professional-multi-function-hair-dryer-n17172/                                       Joy Professional Multi Function Hair Dryer                  Joy     390 ريال   390.00     6          4.8
    71        https://niceonesa.com/ar/care/sunscreen/cetaphil-tinted-sun-50spf-very-high-protection-face-fluid-light-medium-50ml-n17068/  Cetaphil Tinted Sun 50SPF Very High Protection Face Fluid - Light Medium - 50ml             Cetaphil  167.90 ريال   125.93     2          5.0
    72                                 https://niceonesa.com/ar/makeup/eyes/mascara/topface-instyle-rich-curl-mascara-extra-black-n13929/                                 Topface Instyle Rich Curl Mascara - Extra Black               Topface   35.02 ريال    32.00     2          5.0
    73                            https://niceonesa.com/ar/perfume/home-scents/incense-holders/usb-incense-burner-dark-gray-n-231-n17439/                                           USB Incense Burner - Dark Gray - N-231              Niceone  156.98 ريال    49.00    52          4.6
    74                                https://niceonesa.com/ar/makeup/cheek/blush/thebalm-instain-powder-staining-blush-swiss-dot-n16772/                                theBalm Instain Powder Staining Blush - Swiss Dot    theBalm Cosmetics   64.40 ريال    49.00   158          5.0
    75                                           https://niceonesa.com/ar/nails/nails-polish/topface-lasting-color-nail-enamel-033-n8362/                                          Topface Lasting Color Nail Enamel - 033              Topface   18.40 ريال    15.00   169          5.0
    76                                    https://niceonesa.com/ar/care/face-care/tools-and-accessories/stella-derma-roller-system-n1479/                                                       Stella Derma Roller System  Derma roller System   67.85 ر

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Sergey K](https://stackoverflow.com/users/6593287)** (2023-01-10): and to save use - `df.to_csv('name_or_path.csv')`
