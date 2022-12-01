---
title: "How to extract the information from XML beautiful soup?"
site: stackoverflow
question_id: 74642521
url: https://stackoverflow.com/q/74642521
asked: 2022-12-01T13:18:34Z
asked_by: "myamulla_ciencia"
asked_by_url: https://stackoverflow.com/users/9479925
last_edited: never
tags: [python, beautifulsoup]
score: -2
views_at_snapshot: 57
answer_count: 1
accepted_answer_id: 74645871
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c18ac99e5103e67c1df413da3da5af21750fc120e8be0575e425b6c9b7be9946
---

# How to extract the information from XML beautiful soup?

Asked by [myamulla_ciencia](https://stackoverflow.com/users/9479925) on Stack Overflow, <https://stackoverflow.com/q/74642521>, 2022-12-01. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have a list of XML beautifulsoap tag elements as:

```
[
 <Entry>
	<EffectiveDate>
	<DateFormattedForTHForm>07/01/2022</DateFormattedForTHForm>
	</EffectiveDate>
	<ExpirationDate>
	<DateFormattedForTHForm>07/01/2023</DateFormattedForTHForm>
	</ExpirationDate>
	<FormDescription>Notification Of Settlement</FormDescription>
	<FormNumber>WC 99 06 04</FormNumber>
 </Entry>,
 
 <Entry>
 <AccountContactRole>
 <AccountContact>
	<Contact>
	<DisplayName>Mallesham Yamulla</DisplayName>
	<FEINOrSSN>123-45-6789</FEINOrSSN>
	<formsMaskedSSN_and_NoMaskFEIN>**-***-8834</formsMaskedSSN_and_NoMaskFEIN>
	<PrimaryAddress>
	<AddressLine1>A</AddressLine1>
	<AddressLine123>B</AddressLine123>
	<CityStateZip>ENID, OK 73703</CityStateZip>
	<Country>IND</Country>
	<AddressLine2 xsi:nil="true"/>
	<AddressLine3 xsi:nil="true"/>
	</PrimaryAddress>
	</Contact>
	</AccountContact>
	</AccountContactRole>
 </Entry>
 
 ]
``` 

Here I would like to loop through the list of entry xml elements, get a tag name and its contained information's, if any of tag is empty and its information is also empty it should be ignored.

From first entry the below tag information is required to be extracted as they hold on information.
```
[<DateFormattedForTHForm>07/01/2022</DateFormattedForTHForm>,
<DateFormattedForTHForm>07/01/2023</DateFormattedForTHForm>,
<FormDescription>Notification Of Settlement</FormDescription>,
<FormNumber>WC 99 06 04</FormNumber>]

```
From second entry:

```
	<DisplayName>Mallesham Yamulla</DisplayName>
	<FEINOrSSN>123-45-6789</FEINOrSSN>
	<formsMaskedSSN_and_NoMaskFEIN>**-***-6789</formsMaskedSSN_and_NoMaskFEIN>
	<PrimaryAddress>
	<AddressLine1>A</AddressLine1>
	<AddressLine123>B</AddressLine123>
	<CityStateZip>ENID, OK 73703</CityStateZip>
	<Country>IND</Country>
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[baduker](https://stackoverflow.com/users/6106791)** (2022-12-01): Please read [ask] and provide a [mre].
- **[Jack Fleeting](https://stackoverflow.com/users/9448090)** (2022-12-01): The xml snippets in your question aren't well formed. If they come from the same document, pleae edit your question and add a sample, well formed, xml (including any namespace declarations).
