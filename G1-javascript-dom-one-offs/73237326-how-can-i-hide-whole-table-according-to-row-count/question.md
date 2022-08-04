---
title: "how can i hide whole table according to row count"
site: stackoverflow
question_id: 73237326
url: https://stackoverflow.com/q/73237326
asked: 2022-08-04T14:04:00Z
asked_by: "Batuğ Can Akpınar"
asked_by_url: https://stackoverflow.com/users/19666023
last_edited: 2022-08-04T14:07:18Z
tags: [javascript, html]
score: 0
views_at_snapshot: 30
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 29e07596bd38c7f2c1dce073472b8527c78710a1c3c16c139a1c5dbc228b0bdd
---

# how can i hide whole table according to row count

Asked by [Batuğ Can Akpınar](https://stackoverflow.com/users/19666023) on Stack Overflow, <https://stackoverflow.com/q/73237326>, 2022-08-04, last edited 2022-08-04. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm working on a project about e-commercial website. I have problem with Cart section. I want to show one table if there is some goods on cart but if there is no i wanna show another table.

Here is my HTML code for tables

        <div class="sepet">
      <div id="dialog" title="Ürün Açıklaması">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit</p>
      </div>
      <table id="sepettablo" align="center" class="roundedCorners">
        <tr>
          <th>Ürün</th>
          <th>Açıklama</th>
          <th>Adet</th>
          <th>Birim Fiyatı</th>
          <th>Fiyat</th>
        </tr>
        <tr>
          <td><img src="images\5.jpg" style="height:100px;" alt="Alternate Text" /></td>
          <td id="aciklama"><span class="opener" style="cursor:pointer;">Lorem ipsum dolor sit amet, consectetur adipiscing elit</span></td>
          <td><i style="cursor:pointer;" onclick="arttir()" class="fa-solid fa-circle-plus"></i> <input type="button" id="sonuc" value="1" /> <i onclick="azalt()" style="cursor:pointer;" class="fa-solid fa-circle-minus"></i> <i style="cursor:pointer;" class="fa-solid fa-trash-can"
              onclick="urunsilme()"></i></td>
          <td>
            <span class="shop-price" style="cursor:default">129.99 TL</span>
          </td>
          <td>4</td>
        </tr>
        <tr>
          <td><img src="images\6.jpg" style="height:100px;" alt="Alternate Text" /></td>
          <td id="aciklama"><span class="opener" style="cursor:pointer;">Lorem ipsum dolor sit amet, consectetur adipiscing elit</span></td>
          <td><i style="cursor:pointer;" onclick="arttir()" class="fa-solid fa-circle-plus"></i> <input type="button" id="sonuc" value="1" /> <i onclick="azalt()" style="cursor:pointer;" class="fa-solid fa-circle-minus"></i> <i style="cursor:pointer;" class="fa-solid fa-trash-can"
              onclick="urunsilme()"></i></td>
          <td>
            <span class="shop-price" style="cursor:default">129.99 TL</span>
          </td>
          <td>4</td>
        </tr>
        <tr>
          <td><img src="images\3.jpg" style="height:100px;" alt="Alternate Text" /></td>
          <td id="aciklama"><span class="opener" style="cursor:pointer;">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</span></td>
          <td><i style="cursor:pointer;" onclick="arttir()" class="fa-solid fa-circle-plus"></i> <input type="button" id="sonuc" value="1" /> <i onclick="azalt()" style="cursor:pointer;" class="fa-solid fa-circle-minus"></i> <i style="cursor:pointer;" class="fa-solid fa-trash-can"
              onclick="urunsilme()"></i></td>
          <td>
            <span class="shop-price" style="cursor:default">129.99 TL</span>
          </td>
          <td>4</td>
        </tr>
        <tr>
          <td><img src="images\4.jpg" style="height:100px;" alt="Alternate Text" /></td>
          <td id="aciklama"><span class="opener" style="cursor:pointer;">Lorem ipsum dolor sit amet, consectetur adipiscing elit</span></td>
          <td><i style="cursor:pointer;" onclick="arttir()" class="fa-solid fa-circle-plus"></i> <input type="button" id="sonuc" value="1" /> <i onclick="azalt()" style="cursor:pointer;" class="fa-solid fa-circle-minus"></i> <i style="cursor:pointer;" class="fa-solid fa-trash-can"
              onclick="urunsilme()"></i></td>
          <td>
            <span class="shop-price" style="cursor:default">129.99 TL</span>
          </td>
          <td>4</td>
        </tr>
        <tr class="toplam">
          <td>&nbsp;</td>
          <td>&nbsp;</td>
          <td>
            <td><i style="cursor:pointer;" onclick="arttir()" class="fa-solid fa-circle-plus"></i> <input type="button" id="sonuc" value="1" /> <i onclick="azalt()" style="cursor:pointer;" class="fa-solid fa-circle-minus"></i> <i style="cursor:pointer;" class="fa-solid fa-trash-can"
                onclick="urunsilme()"></i></td>
            <td>Toplam:</td>
            <td>&nbsp;</td>
        </tr>
      </table>
    
      <table class="sepetbos" align="center">
        <tbody>
          <tr>
            <td><span>Sepetiniz boş. Ürün eklemek ister misiniz?</span></td>
          </tr>
        </tbody>
      </table>
    </div>



there it is. I have a function about deleting rows but it's just deleting rows. I want to disappear all table and show another table (class=sepetbos). and it must be according to the row count (first and last row included)

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Batuğ Can Akpınar](https://stackoverflow.com/users/19666023)** (2022-08-04): i know another question about this topic but it did not helped me on this problem. so please do not close this topic.
