---
title: "Creating dataframe from XML file with non-unique tags"
site: stackoverflow
question_id: 75346930
url: https://stackoverflow.com/q/75346930
asked: 2023-02-04T17:22:32Z
asked_by: "user53526356"
asked_by_url: https://stackoverflow.com/users/6367971
last_edited: never
tags: [python, pandas, xml, beautifulsoup]
score: -1
views_at_snapshot: 121
answer_count: 3
accepted_answer_id: 75348373
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 2fda93bceea0d09e45c10b02031bdfcd0805a7a0d8089b049c6945a114f14ef3
---

# Creating dataframe from XML file with non-unique tags

Asked by [user53526356](https://stackoverflow.com/users/6367971) on Stack Overflow, <https://stackoverflow.com/q/75346930>, 2023-02-04. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have a directory of XML files, and I need to extract 4 values from each file and store to a dataframe/CSV.

The problem is some of the data I need to extract uses redundant tags (e.g., `<PathName>`) so I'm not sure of the best way to do this. I could specify the exact line # to extract, because it appears consistent with the files I have seen; but I am not certain that will always be the case, so doing it that way is too brittle. 

```
<?xml version="1.0" encoding="utf-8"?>
<BxfMessage xsi:schemaLocation="http://smpte-ra.org/schemas/2021/2019/BXF BxfSchema.xsd" id="jffsdfs" dateTime="2023-02-02T20:11:38Z" messageType="Info" origin="url" originType="Delivery" userName="ABC Corp User" destination=" System" xmlns="http://sffe-ra.org/schema/1999/2023/BXF" xmlns:xsi="http://www.w9.org/4232/XMLSchema-instance">
  <BxfData action="Spotd">
    <Content timestamp="2023-02-02T20:11:38Z">
      <NonProgramContent>
        <Details>
          <SpotType>Paid</SpotType>
          <SpotType>Standard</SpotType>
          <Spotvertiser>
            <SpotvertiserName>Spot Plateau</SpotvertiserName>
          </Spotvertiser>
          <Agency>
            <AgencyName>Spot Plateau</AgencyName>
          </Agency>
          <Product>
            <Name></Name>
            <BrandName>zzTop</BrandName>
            <DirectResponse>
              <PhoneNo></PhoneNo>
              <PCode></PCode>
              <DR_URL></DR_URL>
            </DirectResponse>
          </Product>
        </Details>
        <ContentMetSpotata>
          <ContentId>
            <BHGXId idType="CISC" auth="Agency">AAAA1111999Z</BHGXId>
          </ContentId>
          <Name>Pill CC Dutch</Name>
          <Policy>
            <PlatformType>Spotcast</PlatformType>
          </Policy>
          <Media>
            <BaseBand>
              <Audio VO="true">
                <AnalogAudio primAudio="false" />
                <DigitalAudio>
                  <MPEGLayerIIAudio house="false" audioId="1" dualMono="false" />
                </DigitalAudio>
              </Audio>
              <Video withlate="false" sidebend="false">
                <Format>1182v</Format>
                <CCs>true</CCs>
              </Video>
              <AccessServices>
                <AudioDescription_DVS>false</AudioDescription_DVS>
              </AccessServices>
              <QC>Passed QC (AAAA1111103H )</QC>
            </BaseBand>
            <MediaLocation sourceType="Primary">
              <Location>
                <AssetServer PAA="true" FTA="true">
                  <PathName>zzTap_zzTop_AAAA1111999Z_30s_Pill_aa-bb.mp4</PathName>
                </AssetServer>
              </Location>
              <SOM>
                <SmpteTimeCode>00:00:00;00</SmpteTimeCode>
              </SOM>
              <Duration>
                <SmpteDuration>
                  <SmpteTimeCode>00:00:30;00</SmpteTimeCode>
                </SmpteDuration>
              </Duration>
            </MediaLocation>
            <MediaLocation sourceType="Proxy" qualifer="Low-res">
              <Location>
                <AssetServer PAA="true" FTA="true">
                  <PathName>https://app.url.com/DMM/DL/wew52f</PathName>
                </AssetServer>
              </Location>
              <SOM>
                <SmpteTimeCode>00:00:00;00</SmpteTimeCode>
              </SOM>
              <Duration>
                <SmpteDuration>
                  <SmpteTimeCode>00:00:30;00</SmpteTimeCode>
                </SmpteDuration>
              </Duration>
            </MediaLocation>
            <MediaLocation sourceType="Preview" qualifer="Thumbnail">
              <Location>
                <AssetServer PAA="true" FTA="true">
                  <PathName>https://f9-int-5.rainxyz.com/url.com/media/t43fs/423gs-389a-40a4.jpg?inline</PathName>
                </AssetServer>
              </Location>
              <SOM>
                <SmpteTimeCode>00:00:00;00</SmpteTimeCode>
              </SOM>
              <Duration>
                <SmpteDuration>
                  <SmpteTimeCode>00:00:00;00</SmpteTimeCode>
                </SmpteDuration>
              </Duration>
            </MediaLocation>
          </Media>
        </ContentMetSpotata>
      </NonProgramContent>
    </Content>
  </BxfData>
</BxfMessage>
```

Is there a more flexible method so that I can get consistent output like: 

```
FileName	                            Brand	ID	            URL
zzTap_zzTop_AAAA1111999Z_30s_Pill_aa-bb	zzTop	AAAA1111999Z	https://app.url.com/DMM/DL/wew52f
zzTap_zzTab_BAAA1111999Z_30s_Pill_aa-cc	zzTab	BAAA1111999Z	https://app.url.com/DMM/DL/wew52c
zzTap_zzTan_CAAA1111999Z_30s_Pill_aa-dd	zzTan	CAAA1111999Z	https://app.url.com/DMM/DL/wew523
zzTap_zzTon_DAAA1111999Z_30s_Pill_aa-zz	zzTon	DAAA1111999Z	https://app.url.com/DMM/DL/wew52y
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[trigonom](https://stackoverflow.com/users/12829545)** (2023-02-04): how do u know when it's the correct <path name> when opening the file manually? if it's by the parent tag, iterate to it first, if it's by the form of the content validate it, etc
