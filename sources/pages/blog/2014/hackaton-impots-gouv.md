title: Un hackaton pour (re)penser impôts.gouv.fr
date: 2014-06-27
published: true


Ce dernier mercredi de juin a eu lieu le hackaton de impots.gouv.fr.
Un événement plutôt surprenant auquel, en tant que contribuable, citoyen et développeur, il était de bon sens de participer.
Et c'est sans regret. L'événement se passait dans l'atypique salle de TheFamily, proche de la Bastille. Une cinquantaine de personnes, principalement des profils développeurs, marketing, UX-design, mais aussi des internes en masse de la Direction Générale des Finances Publiques.


### DGFiP et confessions

Parmi la DGFiP des développeurs, des webmasters, des gestionnaires ainsi que des directeurs. La structure interne nous est annoncée comme une trop forte hiérarchie qui en fait leur talon d'Achille, et un vaste méli-mélo. Ils témoignent des lourdeurs en interne, de la lenteur des décisions de par la structure pyramidale, de la rigidité de trop de décideurs, leur honte auprès de leur proches dans la complexité d'être contribuable, du manque de culture sur des méthodes adaptatives (ils en sont toujours à l'époque cahier "décharge").
Ils confessent avoir mis 12 ans pour avoir la plateforme existante, déjà obsolète dès la commande, jeter l'argent par la fenêtre du jour de la signature avec les grandes SSII de ce pays (leurs noms sont ouvertement cités à la conf) en sachant que dès la signature, "ils n'en auront pas pour leur argent, et pourtant il y en a de l'argent de posé".
Si l'on peut témoigner de tout ceci, c'est aussi parce qu'on pouvait sentir une franche intention de changement chez la plupart de la DGFiP, un appel à l'aide et à l'inspiration, une volonté de sortir de ces sillons. Un besoin d'air frais et de nouveau. Ils veulent ce changement, et pas dans 12 ans. Ils se sont même tournés à la dérision à la vue d'un dinosaure pour le photographier en s'amusant d'en faire leur mascotte.
Les messages étaient forts, sans concession, sans demi-mots.


### la journée

Alors, ont-ils eu ce qu'ils voulaient ? Il me semble pouvoir dire oui. Ils paraissaient satisfaits à la hauteur de l'investissement des 10 équipes constituées à ce hackaton lors de cette journée. Tout le monde a joué le jeu jusqu'au bout.
Les travaux délivrés étaient de bonne qualité et les présentations pêchues.
On aurait pu se croire à un startupweekend auquel on aurait remplacé la couche bullshitesque du prévisionnel par de l'intention et de la souplesse, l'assoiffement financier par la participation co-citoyenne, et les jugements du jury incompétent par une écoute impliquée.


### Open API

Le projet sur lequel j'ai choisi de consacrer ma journée était l'implémentation d'une open API qui exposerait les données de impots.gouv.fr en HTTP. L'idée est donc de permettre d'accéder en lecture à un ensemble de données d'un contribuable, de sa déclaration, calendrier, ou aux données générales du Trésor Public, mais également de participer à ces données. L'intérêt pourrait être d'envisager des plateformes indépendantes et spécialisées dans une tâche pointue. Par exemple si j'ai fait de nombreux dons à certaines associations, une app me permettrait de les renseigner. Ma déclaration pré-remplirait les cases adéquates en récupérant directement ces données du service compatible. Un autre exemple serait une interface de remplissage optimisée revenus BNC, via une application dédiée, et renseignerait directement la déclaration d'impôts.

Les intérêts sont nombreux :

- expertiser la DGFiP sur la détention, la sécurisation, l'exploitation et le contrôle des données ;
- les décharger d'une partie des interfaces ;
- permettre à des entreprises, startups, scop, développeurs, de fabriquer leurs propres apps ;
- offrir un vrai choix d'interfaces au contribuable.

En déchargeant la DGFiP des applications, on leur permet donc de s'axer sur l'essentiel, la donnée.
Leur lenteur procédurière ne leur permettant pas de faire face au monde mouvant du web, ils pourraient alors décharger les interfaces, l'ergonomie, le design et la convivialité à des externes. On pourrait tout de même imaginer conserver des applis internes aux impôts (probablement l'existante actuelle) qui auraient pour sens de couvrir des besoins non implémentés en externe, ou pour une consultation éventuelle "officielle" de ce qui en est généré.


### Et la suite ?

On verra prochainement si ce hackaton est à rajouter à http://hackathonbullshit.tumblr.com/ ou si la volonté de travailler avec des entreprises à taille humaine sur des mini-plateformes est réelle.
La vision que j'en ai est que les idées de ce hackaton sont une source d'inspiration pour faire changer les choses. On ne parle pas d'argent, et peut importe qui s'occupe de la réalisation.
La vraie question est : verra-t-on enfin le jour de api.impots.gouv.fr ?
La peine du quotidien des fonctionnaires de la DGFiP a-t-elle déjà repris le dessus ? La lourdeur hiérarchique va t'elle continuer à freiner les innovations ?
La DGFiP va t'elle enfin permettre au contribuable de contribuer ?


### Liens

Des ressources disponibles :

- le speech de présentation : [http://forum.journaldupirate.com/viewtopic.php?f=40&t=8864&p=70876#p70850](http://forum.journaldupirate.com/viewtopic.php?f=40&t=8864&p=70876)
- les ressources fournies : [http://www2.impots.gouv.fr/telechargement/ux-camp/dgfip.html#elem](http://www2.impots.gouv.fr/telechargement/ux-camp/dgfip.html)
- de l'inspiration britannique : [https://github.com/alphagov](https://github.com/alphagov)
- un portail où pourrait figurer la France : [https://government.github.com/](https://government.github.com)
- les slides et leur annexe (prochainement).
- et peut-être un jour api.impots.gouv.fr (si ce n'est plus une 404, on débouche le jus de pomme).
