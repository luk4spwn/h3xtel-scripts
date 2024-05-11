We are provided with the following statement.

```
Title: Frecuency Hacker

Description: Can you crack this substitution cipher? ;)
Author: D-Cryp7

Encrypted flag: 'hppdlidt tuyxhf da tyzlicrynlwz iwhz fwcupe kh lyhiiz fdqlph ydrwi da n yhthai lnlhy n rycul cv lwzfdtdfif ni tnqkyderh uadxhyfdiz lyhfhaihe na hsnqlph cv na hppdlidt tuyxh da jwdtw n tyzlicrynlwdt clhynicy inbhf n fhi cv auqkhyf daic nttcuai iwha ufhf iwcfh auqkhyf ic lycxh iwni iwh ahj bhz wnf khha lyceuthe kui iwdf df aci na hsnqlph cv iwh lhyvhti nprcydiwq iwni fcpxhf hxhyz tcathdxnkph lyckphq hflhtdnppz aci vcy hatyzlidca khtnufh di phnxhf cui cah fqnpp lnyi iwh qniwhqnidtnp vcyqupnidca iwni df ntiunppz ufhe ic rhahynih iwh yhfupi iwh lyckphq df iwni iwh nprcydiwq df aci ntiunppz n lhyvhti nprcydiwq di echfai ahthffnydpz ufh iwh ydrwi fhi cv auqkhyf kui iwh nafjhy df iwni iwhyh nyh ni phnfi fhxhynp jnzf ic fcpxh iwni vuatidca cah cv iwcfh ufhf tna kh ehydxhe vycq iwh aniuynp auqkhyf iwhqfhpxhf jwhyh zcu wnxh n fhmuhath cv auqkhyf iwni cah fhhf nf wnxdar qcyh iwna cah xnpuh wh hslpndaheiwh lyckphq df iwni capz thyinda fcpuidcaf ufdar naz cv iwh edvvhyhai fzqkcpf tna ntiunppz lyceuth iwh tcyyhti enin iwni qhnaf iwni dif dqlcffdkph ic tcqh ul jdiw lhyvhti auqkhyf da rhahynp jwha iwh tcyyhti nafjhy df n tcqlphihpz nykdiynyz fhi cv auqkhyfn lyckphq pdbh iwdf df aci gufi n qniwhqnidtnp cah nae iwhyh df n twnath iwni qcfi tyzlicrynlwdt vuatidcaf jdiw qupidlph auqkhyf cv clhynidcaf futw nf iwh yfn nprcydiwq tcupe kh dqlycxhe jdiw iwhdy nprcydiwqf kz fdqlpz twnardar iwh auqkhyf cv clhynidca da iwh hae di jcupe qnbh fhafh ic phnxh iwh qniwhqnidtf nae lyckphqf cv jwz iwdf df iyuh aci khdar edftuffhe'
```

In the description we are given the clue that the text was encrypted using a substitution cipher, that is to say that each letter of the cipher is replaced by one and encrypted on that basis.

The first thing I did was to send the text to a frequency analysis tool, what this tool does is to report me the most repeated letters in the text, with this result I can see the most used letters in the text and replace them little by little to see if I can build words.

![](https://i.imgur.com/IesXnzo.png)

> You have to use a lot of logic in this type of challenges, for example if we know that in English the word `the` is repeated a lot, we could replace the 3 letters that are most repeated by this word.

Based on the frequency results I programmed the following script and was able to see the decoded text.

``` python
ct = "hppdlidt tuyxhf da tyzlicrynlwz iwhz fwcupe kh lyhiiz fdqlph ydrwi da n yhthai lnlhy n rycul cv lwzfdtdfif ni tnqkyderh uadxhyfdiz lyhfhaihe na hsnqlph cv na hppdlidt tuyxh da jwdtw n tyzlicrynlwdt clhynicy inbhf n fhi cv auqkhyf daic nttcuai iwha ufhf iwcfh auqkhyf ic lycxh iwni iwh ahj bhz wnf khha lyceuthe kui iwdf df aci na hsnqlph cv iwh lhyvhti nprcydiwq iwni fcpxhf hxhyz tcathdxnkph lyckphq hflhtdnppz aci vcy hatyzlidca khtnufh di phnxhf cui cah fqnpp lnyi iwh qniwhqnidtnp vcyqupnidca iwni df ntiunppz ufhe ic rhahynih iwh yhfupi iwh lyckphq df iwni iwh nprcydiwq df aci ntiunppz n lhyvhti nprcydiwq di echfai ahthffnydpz ufh iwh ydrwi fhi cv auqkhyf kui iwh nafjhy df iwni iwhyh nyh ni phnfi fhxhynp jnzf ic fcpxh iwni vuatidca cah cv iwcfh ufhf tna kh ehydxhe vycq iwh aniuynp auqkhyf iwhqfhpxhf jwhyh zcu wnxh n fhmuhath cv auqkhyf iwni cah fhhf nf wnxdar qcyh iwna cah xnpuh wh hslpndaheiwh lyckphq df iwni capz thyinda fcpuidcaf ufdar naz cv iwh edvvhyhai fzqkcpf tna ntiunppz lyceuth iwh tcyyhti enin iwni qhnaf iwni dif dqlcffdkph ic tcqh ul jdiw lhyvhti auqkhyf da rhahynp jwha iwh tcyyhti nafjhy df n tcqlphihpz nykdiynyz fhi cv auqkhyfn lyckphq pdbh iwdf df aci gufi n qniwhqnidtnp cah nae iwhyh df n twnath iwni qcfi tyzlicrynlwdt vuatidcaf jdiw qupidlph auqkhyf cv clhynidcaf futw nf iwh yfn nprcydiwq tcupe kh dqlycxhe jdiw iwhdy nprcydiwqf kz fdqlpz twnardar iwh auqkhyf cv clhynidca da iwh hae di jcupe qnbh fhafh ic phnxh iwh qniwhqnidtf nae lyckphqf cv jwz iwdf df iyuh aci khdar edftuffhe"

ct = ct.replace("h", "E")
ct = ct.replace("i", "T")
ct = ct.replace("w", "H")
ct = ct.replace("n", "A")
ct = ct.replace("a", "N")
ct = ct.replace("e", "D")
ct = ct.replace("q", "M")
ct = ct.replace("d", "I")
ct = ct.replace("t", "C")
ct = ct.replace("p", "L")
ct = ct.replace("y", "R")
ct = ct.replace("x", "V")
ct = ct.replace("f", "S")
ct = ct.replace("r", "G")
ct = ct.replace("c", "O")
ct = ct.replace("u", "U")
ct = ct.replace("k", "B")
ct = ct.replace("j", "W")
ct = ct.replace("z", "Y")
ct = ct.replace("l", "P")
ct = ct.replace("v", "F")
ct = ct.replace("s", "X")
ct = ct.replace("m", "C")


print(ct)
```

```
ELLIPTIC CURVES IN CRYPTOGRAPHY THEY SHOULD BE PRETTY SIMPLE RIGHT IN A RECENT PAPER A GROUP OF PHYSICISTS AT CAMBRIDGE UNIVERSITY PRESENTED AN EXAMPLE OF AN ELLIPTIC CURVE IN WHICH A CRYPTOGRAPHIC OPERATOR TAbES A SET OF NUMBERS INTO ACCOUNT THEN USES THOSE NUMBERS TO PROVE THAT THE NEW bEY HAS BEEN PRODUCED BUT THIS IS NOT AN EXAMPLE OF THE PERFECT ALGORITHM THAT SOLVES EVERY CONCEIVABLE PROBLEM ESPECIALLY NOT FOR ENCRYPTION BECAUSE IT LEAVES OUT ONE SMALL PART THE MATHEMATICAL FORMULATION THAT IS ACTUALLY USED TO GENERATE THE RESULT THE PROBLEM IS THAT THE ALGORITHM IS NOT ACTUALLY A PERFECT ALGORITHM IT DOESNT NECESSARILY USE THE RIGHT SET OF NUMBERS BUT THE ANSWER IS THAT THERE ARE AT LEAST SEVERAL WAYS TO SOLVE THAT FUNCTION ONE OF THOSE USES CAN BE DERIVED FROM THE NATURAL NUMBERS THEMSELVES WHERE YOU HAVE A SECUENCE OF NUMBERS THAT ONE SEES AS HAVING MORE THAN ONE VALUE HE EXPLAINEDTHE PROBLEM IS THAT ONLY CERTAIN SOLUTIONS USING ANY OF THE DIFFERENT SYMBOLS CAN ACTUALLY PRODUCE THE CORRECT DATA THAT MEANS THAT ITS IMPOSSIBLE TO COME UP WITH PERFECT NUMBERS IN GENERAL WHEN THE CORRECT ANSWER IS A COMPLETELY ARBITRARY SET OF NUMBERSA PROBLEM LIbE THIS IS NOT gUST A MATHEMATICAL ONE AND THERE IS A CHANCE THAT MOST CRYPTOGRAPHIC FUNCTIONS WITH MULTIPLE NUMBERS OF OPERATIONS SUCH AS THE RSA ALGORITHM COULD BE IMPROVED WITH THEIR ALGORITHMS BY SIMPLY CHANGING THE NUMBERS OF OPERATION IN THE END IT WOULD MAbE SENSE TO LEAVE THE MATHEMATICS AND PROBLEMS OF WHY THIS IS TRUE NOT BEING DISCUSSED
```

