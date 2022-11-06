---
title: "How to get the text inside a tag using BeautifulSoup in Python"
site: stackoverflow
question_id: 74319795
answer_id: 74334353
url: https://stackoverflow.com/a/74334353
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-06T08:40:13Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74334353/revisions
accepted: true
score: 0
chapter: C2
chapter_title: "Getting clean text out of tags"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 04c135bf391e90420dc5f4457993f3698cfdb7d96f6e48da894c16cb8a853c75
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-06

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74334353>, 2022-11-06; **accepted**; score 0. Text as retrieved 2026-10-12.

The issue is that you're not receiving the fully loaded html\*. You'll get better results if you set the http://agence-prd.ansm.sante.fr/php/ecodex/rcp/R0390743.htm as `link` - it's where the page from your code is fetching and loading its contents from anyway. If you're receiving the link from somewhere else and need to automate the transformation, you can do something like
```python
# link = 'http://agence-prd.ansm.sante.fr/php/ecodex/frames.php?specid=61350428&typedoc=R&ref=R0390743.htm' # your link
linkStart = '/'.join(link.split('/')[:-1])
refParam = link.split('?', 1)[-1].split('ref=',1)[-1].split('&')[0].split('.')[0]
link = f'{linkStart}/rcp/{refParam}.htm' # my link

req = requests.get(link)
soup = BeautifulSoup(req.content)
# rest of your code
```

<hr>

Btw, if you're just getting all the text, you might as well use `soup.body.text` directly, but also, if you want all the texts from the separate `p` tags in one variable, you can use `join` with [list comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp)
```python
pTexts = '\n'.join([p.text for p in soup.findAll('p')])
print(pTexts)
```
- it should have the same output as printing in a loop as you were
```lang-none
RÉSUMÉ DES CARACTÉRISTIQUES DU PRODUIT
ANSM - Mis à jour le : 22/06/2022
1. DENOMINATION DU MEDICAMENT
ZYRTEC 2,5 mg/2,5 ml, solution buvable en flacon
2. COMPOSITION QUALITATIVE ET QUANTITATIVE
Chaque ml de solution buvable en flacon contient 1 mg de dichlorhydrate de cétirizine.
Excipients à effet notoire : 
· un ml de solution contient 450 mg de sorbitol (solution à 70 %, non cristallisable)
· un ml de solution contient 1,35 mg de parahydroxybenzoate de méthyle
· un ml de solution contient 0,15 mg de parahydroxybenzoate de propyle.
Pour la liste complète des excipients, voir rubrique 6.1.
3. FORME PHARMACEUTIQUE
Solution buvable.
Liquide limpide et incolore avec un goût légèrement sucré et un arôme banane.
4. DONNEES CLINIQUES
4.1. Indications thérapeutiques
Le dichlorhydrate de cétirizine 2,5 mg/2,5 ml, solution buvable en flacon est indiqué chez l'adulte et l’enfant à partir de 2 ans :
· dans le traitement des symptômes nasaux et oculaires des rhinites allergiques saisonnières et perannuelles ;
· dans le traitement des symptômes de l'urticaire chronique idiopathique.
4.2. Posologie et mode d'administration
Posologie
10 mg une fois par jour (10 ml de solution buvable (2 cuillères pleines)).
Populations particulières
Sujets âgés
Il n’y a pas lieu d’ajuster la posologie chez le sujet âgé dont la fonction rénale est normale.
Insuffisance rénale
Les données disponibles ne permettent pas de documenter le rapport bénéfice/risque en cas d’insuffisance rénale. Compte tenu de l’élimination essentiellement rénale de la cétirizine (voir rubrique 5.2.), et s’il ne peut être utilisé de traitement alternatif, l'intervalle entre les prises doit être ajusté selon la fonction rénale. La posologie doit être ajustée comme indiqué dans le tableau ci-après. 
Adaptation posologique chez les patients atteints d'insuffisance rénale :
Insuffisance hépatique
Aucun ajustement de la dose n’est nécessaire chez les patients atteints d’insuffisance hépatique isolée. Chez les patients atteints d'insuffisance hépatique associée à une insuffisance rénale, un ajustement de la dose est recommandé (voir rubrique « Insuffisance rénale » ci-dessus).
Population pédiatrique
Enfants de 2 à 6 ans : 2,5 mg deux fois par jour (2,5 ml de solution orale deux fois par jour (une demie cuillère deux fois par jour)).
Enfants de 6 à 12 ans : 5 mg deux fois par jour (5 ml de solution orale deux fois par jour (une cuillère deux fois par jour)).
Adolescents de plus de 12 ans : 10 mg une fois par jour (10 ml de solution orale deux fois par jour (2 cuillères deux fois par jour)).
Chez l’enfant présentant une insuffisance rénale, la posologie sera ajustée individuellement en fonction de la clairance rénale, de l’âge et du poids corporel du patient.
Mode d’administration
La solution peut être avalée telle quelle sans dilution.
4.3. Contre-indications
Hypersensibilité à la substance active ou à l’un des excipients mentionnés à la rubrique 6.1, à l’hydroxyzine ou aux dérivés de la pipérazine.
Patients atteints d’insuffisance rénale en stade terminal avec un taux de filtration glomérulaire (DFG) estimé inférieur à 15 ml/min.
4.4. Mises en garde spéciales et précautions d'emploi
Aux doses thérapeutiques, aucune interaction cliniquement significative n'a été mise en évidence avec la prise d'alcool (pour des concentrations sanguines d'alcool allant jusqu’à 0,5 g/l). Cependant, la prudence est recommandée en cas de prise concomitante d'alcool.
Des précautions doivent être prises chez les patients avec des facteurs prédisposant à la rétention urinaire (par ex. lésion de la moelle épinière, hyperplasie prostatique) étant donné que la cétirizine peut augmenter le risque de rétention urinaire.
La cétirizine doit être administrée avec prudence chez les patients épileptiques ou à risque de convulsions.
Les parahydroxybenzoates de propyle et de méthyle sont susceptibles de provoquer des réactions allergiques (éventuellement retardées).
Les patients présentant une intolérance héréditaire au fructose (IHF) ne doivent pas prendre ce médicament.
La réponse aux tests allergiques cutanés est inhibée par les antihistaminiques et une période de 3 jours sans traitement est nécessaire avant de les réaliser.
Un prurit et/ou une urticaire peuvent se déclarer lors de l’arrêt de la cétirizine, même si les symptômes n’étaient pas présents avant le début du traitement. Dans certains cas, les symptômes peuvent être intenses et nécessiter la reprise du traitement. Les symptômes devraient disparaître lors de la reprise du traitement.
Population pédiatrique
En raison de la quantité de certains excipients dans la composition, l’utilisation de ce médicament n’est pas recommandée chez l’enfant de moins de 2 ans.
4.5. Interactions avec d'autres médicaments et autres formes d'interactions
Compte tenu des données de pharmacocinétique, de pharmacodynamie et du profil de tolérance de la cétirizine, aucune interaction n’est attendue avec cet antihistaminique. À ce jour, aucune interaction pharmacodynamique ou pharmacocinétique significative n'a été rapportée lors des études d'interactions médicamenteuses réalisées notamment avec la pseudoéphédrine ou la théophylline (400 mg/jour).
Le taux d’absorption de la cétirizine n’est pas diminué par l’alimentation, bien que la vitesse d’absorption soit réduite.
La prise concomitante d'alcool ou d'autres dépresseurs du système nerveux central (SNC) peut entraîner une altération de la vigilance ou des performances chez les patients sensibles, bien que la cétirizine ne potentialise pas les effets de l’alcool (à une concentration sanguine de 0,5 g/l).
4.6. Fertilité, grossesse et allaitement
Grossesse
Les données prospectives recueillies concernant l’issue des grossesses exposées à la cétirizine ne suggèrent pas un potentiel toxique maternel ou embryo-fœtal supérieur à celui de la population générale.
Les études menées chez l’animal n’ont pas révélé d’effet néfaste direct ou indirect sur la gestation, le développement embryonnaire et fœtal, la parturition et le développement post-natal.
La prudence est recommandée lors de la prescription chez la femme enceinte.
Allaitement
La cétirizine passe dans le lait maternel. Un risque d’effets indésirables chez les nouveau-nés allaités ne peut pas être exclu. La cétirizine est excrétée dans le lait maternel humain à des concentrations de l’ordre de 25 % à 90 % de celles mesurées dans le plasma, selon le moment du prélèvement par rapport à l’administration. Par conséquent, la prudence est recommandée lors de la prescription de cétirizine chez la femme qui allaite.
Fertilité
Les données relatives à la fertilité humaine sont limitées mais aucun risque n’a été identifié.
Les données chez l’animal ne montrent pas de problème de sécurité pour la reproduction humaine.
4.7. Effets sur l'aptitude à conduire des véhicules et à utiliser des machines
Des mesures objectives de la capacité à conduire, du délai d’endormissement et des performances sur lignes d’assemblage n’ont pas démontré d’effets cliniquement pertinents à la dose recommandée de 10 mg. Cependant, les patients ressentant une somnolence ne devraient pas conduire de véhicules, prendre part à des activités potentiellement dangereuses ou utiliser des machines. Ils ne devraient pas dépasser la dose recommandée et devraient tenir compte de leur réponse au médicament. 
4.8. Effets indésirables
Essais cliniques
Synthèse
Des effets indésirables sans gravité sur le système nerveux central, incluant somnolence, fatigue, sensations vertigineuses et céphalées ont été observés au cours des essais cliniques réalisés avec la cétirizine à la dose recommandée. Dans quelques cas, un effet paradoxal de stimulation du système nerveux central a été observé.
Malgré un effet antagoniste sélectif des récepteurs H1 périphériques et une relativement faible activité anticholinergique, des cas isolés de difficulté mictionnelle, de problèmes d'accommodation et de sécheresse buccale ont été rapportés.
Des cas d’anomalies de la fonction hépatique avec augmentation des enzymes hépatiques associée à une augmentation de la bilirubine ont été rapportés. Les anomalies ont régressé dans la plupart des cas avec l’arrêt du traitement par le dichlorhydrate de cétirizine.
Liste des effets indésirables
Plus de 3 200 sujets exposés à la cétirizine ont été inclus dans les essais cliniques contrôlés en double aveugle comparant la cétirizine à la posologie recommandée de 10 mg par jour, au placebo ou à d'autres antihistaminiques, pour lesquels des données quantifiées de tolérance sont disponibles.
Les effets indésirables rapportés sous cétirizine 10 mg pour l’ensemble de cette population au cours des essais contrôlés versus placebo, avec une incidence de 1,0 % ou plus, ont été les suivants :
La somnolence était statistiquement plus fréquente que sous placebo, mais d'intensité légère à modérée dans la majorité des cas. Des tests objectifs, validés par d'autres études, ont montré, chez le jeune volontaire sain, que les activités quotidiennes habituelles ne sont pas affectées à la dose journalière recommandée.
Population pédiatrique
Les effets indésirables rapportés avec une incidence de 1 % ou plus chez les enfants âgés de 6 mois à 12 ans inclus dans les essais cliniques contrôlés versus placebo sont les suivants :
Effets indésirables rapportés depuis la commercialisation
En plus des effets indésirables rapportés au cours des essais cliniques et listés ci-dessus, les effets indésirables suivants ont été rapportés depuis la commercialisation du produit.
Les effets indésirables sont décrits selon la convention MedDRA des classes de systèmes d’organes et par une estimation de leur fréquence depuis la commercialisation.
Les fréquences sont définies de la manière suivante : très fréquent (≥ 1/10) ; fréquent (≥ 1/100, < 1/10) ; peu fréquent (≥ 1/1 000, < 1/100) ; rare (≥ 1/10 000, < 1/1 000) ; très rare (< 1/10 000) ; fréquence indéterminée (ne peut être estimée sur la base des données disponibles).
Affections hématologiques et du système lymphatique
Très rare : thrombocytopénie
Affections du système immunitaire
Rare : hypersensibilité
Très rare : choc anaphylactique
Troubles du métabolisme et de la nutrition
Fréquence indéterminée : augmentation de l’appétit
Affections psychiatriques
Peu fréquent : agitation
Rare : agressivité, confusion, dépression, hallucination, insomnie
Très rare : tics
Fréquence indéterminée : idées suicidaires, cauchemars
Affections du système nerveux
Peu fréquent : paresthésie
Rare : convulsions
Très rare : dysgueusie, syncope, tremblements, dystonie, dyskinésie
Fréquence indéterminée : amnésie, troubles de la mémoire
Affections oculaires
Très rare : troubles de l'accommodation, vision floue, crises oculogyres
Affections de l’oreille et du labyrinthe
Fréquence indéterminée : vertige
Affections cardiaques
Rare : tachycardie
Affections gastro-intestinales
Peu fréquent : diarrhée
Affections hépatobiliaires
Rare : anomalie du bilan hépatique (augmentation des enzymes hépatiques : transaminases, phosphatases alcalines, gamma-GT et bilirubine)
Fréquence indéterminée : hépatite
Affections de la peau et du tissu sous-cutané
Peu fréquent : prurit, éruption cutanée
Rare : urticaire
Très rare : œdème angioneurotique, érythème pigmenté fixe
Indéterminée : pustulose exanthématique aiguë généralisée
Affections musculosquelettiques et du tissu conjonctif
Fréquence indéterminée : arthralgie, myalgie
Affections du rein et des voies urinaires
Très rare : dysurie, énurésie
Fréquence indéterminée : rétention urinaire
Troubles généraux et anomalies au site d'administration
Peu fréquent : asthénie, malaise
Rare : œdème
Fréquence indéterminée : syndrome de sevrage, y compris prurit et démangeaisons
Investigations
Rare : prise de poids.
Description de certains effets indésirables
Des cas de prurit (démangeaisons intenses) et/ou d’urticaire ont été rapportés après l’arrêt du traitement par cétirizine. 
Déclaration des effets indésirables suspectés 
La déclaration des effets indésirables suspectés après autorisation du médicament est importante. Elle permet une surveillance continue du rapport bénéfice/risque du médicament. Les professionnels de santé déclarent tout effet indésirable suspecté via le système national de déclaration : Agence nationale de sécurité du médicament et des produits de santé (ANSM) et réseau des Centres Régionaux de Pharmacovigilance - Site internet : www.signalement-sante.gouv.fr.
4.9. Surdosage
Symptômes
Les symptômes observés après un surdosage de cétirizine sont principalement associés à des effets sur le système nerveux central (SNC) ou des effets suggérant une action anticholinergique.
Les effets indésirables rapportés après la prise d'une dose au moins 5 fois supérieure à la dose quotidienne recommandée sont : confusion, diarrhée, sensations vertigineuses, fatigue, céphalées, malaise, mydriase, prurit, agitation, sédation, somnolence, stupeur, tachycardie, tremblements et rétention urinaire.
Conduite à tenir
Il n'existe pas d'antidote connu spécifique à la cétirizine.
En cas de surdosage, un traitement symptomatique ou des mesures de soutien sont recommandés. Un lavage gastrique peut être envisagé en cas d'ingestion récente.
La cétirizine n'est pas éliminée efficacement par hémodialyse.
5. PROPRIETES PHARMACOLOGIQUES
5.1. Propriétés pharmacodynamiques
Classe pharmacothérapeutique : Antihistaminiques à usage systémique, dérivés de la pipérazine, code ATC : R06AE07.
Mécanisme d’action
La cétirizine, métabolite humain de l'hydroxyzine, est un antagoniste puissant et sélectif des récepteurs H1 périphériques. Des études in vitro de liaison aux récepteurs n'ont pas révélé d’affinité mesurable pour d'autres récepteurs que les récepteurs H1.
Effets pharmacodynamiques
En association aux effets anti-H1, il a été démontré que la cétirizine présente une activité anti-allergique : administrée à la dose de 10 mg une ou deux fois par jour, elle inhibe la phase retardée de recrutement des éosinophiles au niveau de la peau et du tissu conjonctif des sujets atopiques soumis à des tests de provocation allergénique.
Efficacité et sécurité clinique
Les études menées chez le volontaire sain ont montré que la cétirizine, aux doses de 5 et 10 mg, inhibe fortement les réactions érythémato-papuleuses induites par des concentrations très élevées d'histamine au niveau de la peau. Cependant, la corrélation de l'efficacité avec ces observations n'est pas établie.
Dans une étude contrôlée versus placebo menée pendant six semaines chez 186 patients présentant une rhinite allergique et un asthme léger à modéré, la cétirizine 10 mg une fois par jour a amélioré les symptômes de la rhinite sans effet sur les fonctions pulmonaires. Cette étude met en évidence la sécurité d'emploi de la cétirizine chez les patients allergiques ayant un asthme léger à modéré.
Dans une étude contrôlée versus placebo, la cétirizine administrée à la dose quotidienne élevée de 60 mg pendant 7 jours n'a pas entraîné d’allongement statistiquement significatif de l'intervalle QT.
À la posologie recommandée, une amélioration de qualité de vie a été démontrée chez des patients traités par cétirizine ayant une rhinite allergique perannuelle et saisonnière.
Population pédiatrique
Dans une étude de 35 jours menée chez des enfants de 5 à 12 ans, il n’a pas été observé de diminution de l'effet antihistaminique (inhibition de l’érythème et des papules) de la cétirizine. À l'arrêt du traitement par la cétirizine après administration de doses répétées, la réactivité de la peau à l’histamine est rétablie en 3 jours.
5.2. Propriétés pharmacocinétiques
Absorption
Le pic des concentrations plasmatiques mesuré à l’état d’équilibre est d'environ 300 ng/ml et est atteint en 1,0 ± 0,5 h. La distribution des valeurs mesurées des paramètres pharmacocinétiques, tels que le pic plasmatique (Cmax) et l'aire sous la courbe (AUC), est unimodale. 
La biodisponibilité de la cétirizine n'est pas modifiée par la prise alimentaire, bien que la vitesse d'absorption soit diminuée. La biodisponibilité de la cétirizine est équivalente lorsque la cétirizine est administrée sous forme de solution, gélule ou comprimé.
Distribution
Le volume apparent de distribution est de 0,50 l/kg. La liaison aux protéines plasmatiques de la cétirizine est de 93 ± 0,3 %. La cétirizine ne modifie pas la liaison de la warfarine aux protéines.
Biotransformation
La cétirizine ne subit pas d'effet important de premier passage hépatique. 
Élimination
La demi-vie plasmatique terminale de la cétirizine est d'environ 10 heures et aucune accumulation de cétirizine n’est observée après administration de doses journalières de 10 mg pendant 10 jours. Environ les deux tiers de la dose administrée sont éliminés sous forme inchangée dans les urines. 
Linéarité/non-linéarité
La cinétique de la cétirizine est linéaire pour des doses comprises entre 5 et 60 mg.
Insuffisance rénale : la pharmacocinétique de la molécule était similaire chez les patients ayant une insuffisance rénale légère (clairance de la créatinine supérieure à 40 ml/min) et chez les volontaires sains. Chez les patients avec une insuffisance rénale modérée, la demi-vie était augmentée d’un facteur de 3 et la clairance était diminuée de 70 % par rapport aux volontaires sains.
Chez les patients hémodialysés (clairance de la créatinine inférieure à 7 ml/min), la demi-vie était augmentée d’un facteur de 3 et la clairance était diminuée de 70 % par rapport aux sujets sains après administration d’une dose orale unique de 10 mg de cétirizine. La cétirizine n’était que très faiblement éliminée par hémodialyse. Un ajustement de la posologie est nécessaire en cas d'insuffisance rénale modérée ou sévère (voir rubrique 4.2).
Insuffisance hépatique : chez des patients atteints de maladies chroniques du foie (cirrhose d’origine hépatocellulaire, cholestatique et biliaire) recevant une dose unique de 10 ou 20 mg de cétirizine, la demi-vie était augmentée de 50 % avec une diminution de 40 % de la clairance comparativement aux sujets sains.
L'ajustement de la posologie est nécessaire en cas d'insuffisance hépatique seulement en cas d'insuffisance rénale associée.
Sujets âgés : après administration orale d'une dose unique de 10 mg de cétirizine chez 16 sujets âgés, la demi-vie a augmenté d'environ 50 % et la clairance a diminué de 40 % en comparaison aux sujets plus jeunes. La diminution de la clairance de la cétirizine chez ces sujets volontaires âgés semble liée à l'altération de leur fonction rénale.
Population pédiatrique : la demi-vie de la cétirizine est d'environ 6 heures chez les enfants de 6 à 12 ans et de 5 heures chez les enfants de 2 à 6 ans. Chez les nourrissons et les jeunes enfants âgés de 6 à 24 mois, celle-ci est réduite à 3,1 heures.
5.3. Données de sécurité préclinique
Les données non cliniques issues des études conventionnelles de pharmacologie de sécurité, toxicologie en administration répétée, génotoxicité, cancérogénèse, et des fonctions de reproduction et de développement, n’ont pas révélé de risque particulier pour l’homme.
6. DONNEES PHARMACEUTIQUES
6.1. Liste des excipients
Solution de sorbitol à 70 % (non cristallisable) (E420), glycérol, propylène glycol, saccharine sodique, parahydroxybenzoate de méthyle (E218), parahydroxybenzoate de propyle (E216), arôme banane 54.330/A (Firmenich), acétate de sodium, acide acétique glacial, eau purifiée.
6.2. Incompatibilités
Sans objet.
6.3. Durée de conservation
5 ans.
Après ouverture : 3 mois.
6.4. Précautions particulières de conservation
Ce médicament ne nécessite pas de précautions particulières de conservation.
6.5. Nature et contenu de l'emballage extérieur 
Flacon en verre brun (Type III Ph. Eur.) de 60, 75, 100, 150 ou 200 ml fermé par un bouchon de sécurité enfant en polypropylène blanc.
Une cuillère-mesure de 5 ml graduée à 2,5 ml est fournie avec le flacon.
Toutes les présentations peuvent ne pas être commercialisées.
6.6. Précautions particulières d’élimination et de manipulation
Pas d’exigences particulières.
Tout médicament non utilisé ou déchet doit être éliminé conformément à la réglementation en vigueur.
7. TITULAIRE DE L’AUTORISATION DE MISE SUR LE MARCHE
UCB PHARMA S.A.
DEFENSE OUEST
420 RUE ESTIENNE D’ORVES
92700 COLOMBES
8. NUMERO(S) D’AUTORISATION DE MISE SUR LE MARCHE
· 34009 332 924 9 2 : 150 ml en flacon (verre brun) avec cuillère-mesure (polystyrène)
· 34009 333 019 8 9 : 60 ml en flacon (verre brun) avec cuillère-mesure (polystyrène)
9. DATE DE PREMIERE AUTORISATION/DE RENOUVELLEMENT DE L’AUTORISATION
[à compléter ultérieurement par le titulaire]
10. DATE DE MISE A JOUR DU TEXTE
[à compléter ultérieurement par le titulaire]
11. DOSIMETRIE
Sans objet.
12. INSTRUCTIONS POUR LA PREPARATION DES RADIOPHARMACEUTIQUES
Sans objet.
CONDITIONS DE PRESCRIPTION ET DE DELIVRANCE
Liste II.
```

<hr><hr>

\*<sub>[For when you're not getting the expected output from a `requests`+`BeautifulSoup` scrape,] you should make a habit to check that `req.status==200` (it was, in this case, but it might not always be), and then save the fetched html with `with open('x.html', 'wb') as f: f.write(req.content)` - after running, you should open and inspect the "x.html" file; if it does not contain the same html as the page you want to scrape, you should go back to the original page, go to the [network tab](https://help.fullstory.com/hc/en-us/articles/360020623654-How-do-I-use-the-Network-view-in-Dev-Tools-) and see if you can find and replicate the request/s that are being used to fetch the data you want.</sub>

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[yuttokb2](https://stackoverflow.com/users/19953142)** (2022-11-07): Hey Driftr95, thanks a lot for your answer, it has helped me a lot. I just don't quite get the reason why the website's html code was not being fully loaded. This is the first time something like this has happened to me, I have always done the request.content from the website link and I was good to go. From your answer I saw that you formatted the link I provided and it leads to the same website but without the leftMenu panel. How did you know that was the way to format the link? Sorry if I am asking dumb questions, I am still pretty new at this.
- **me** (2022-11-07): @yuttokb2 glad it helped =)  [I explained very briefly in small text at the bottom of the answer as I was not sure how much you already knew.] Some sites have [dynamic pages](https://www.packetlabs.net/posts/dynamic-pages/) which use javascript to load their contents; often, that javascript calls [APIs](https://medium.com/@perrysetgo/what-exactly-is-an-api-69f36968a41f) to get the data for the contents. You can see all the requests made by a page from the [network tab](https://help.fullstory.com/hc/en-us/articles/360020623654-How-do-I-use-the-Network-view-in-Dev-Tools-) in dev tools
- **me** (2022-11-07): (that's where I [saw](https://i.sstatic.net/AVFUk.png) that the "formatted" link was being used to fetch nearly all of the text in the body)
