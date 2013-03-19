title: "Applications mobile : Web vs. Natif"
date: 2013-03-14
published: true

Nous avons récemment eu à enrichir une application Web d’intranet afin d’aménager un accès pour des utilisateurs de mobiles (parc de périphériques connu et contrôlé). Trois approches étaient possibles :

- l’utilisation d’un [*responsive design*](https://fr.wikipedia.org/wiki/Responsive_Web_Design) sur la version Web pour réutiliser l’existant mais cela posait des problèmes de performances (chargement inutile de l’intégralité du HTML et des ressources de la page, mise en cache complexe) ;
- l’utilisation de code natif — ou d’un intermédiaire comme [Titanium](http://www.appcelerator.com/platform/titanium-sdk/) pour bénéficier de la réactivité et des APIs — mais cela nous liait trop fortement aux plateformes propriétaires ;
- l’utilisation d’une version Web dédiée aux périphériques à petits écrans, c’est celle pour laquelle nous avons opté en misant sur la pérennité et l’évolutivité d’une telle approche.

Rapidement, nous avons été confrontés à plusieurs problèmes que nous souhaitions partager avec vous :

## La réactivité

C’était la grande inconnue et nous avons rapidement opté pour une architecture permettant de servir les données en [JSON](http://json.org/) via une API HTTP pour alimenter une application JavaScript en [Backbone.js](http://backbonejs.org/) avec la possibilité de mettre en cache les données côté client (utile lorsque la connexion est aléatoire !).

La latence perceptible au *tap* sur un périphérique iOS pour afficher une page Web s’explique par une préconisation Apple à [à patienter 300ms](http://cubiq.org/remove-onclick-delay-on-webkit-for-iphone) avant de prendre en compte l’action de l’utilisateur ; cela nous semblait trop important compte-tenu de la cible. Des solutions techniques comme celle proposée par la bilbliothèque [FastClick] permettent heureusement de s’affranchir d’une telle contrainte.

Côté performance et réactivité des interfaces, si nous (et notre client) sommes satisfaits des résultats obtenus vis à vis des usages cibles sur leur parc de machines (iPhone 5, iPad et machine Android récentes), il semble pour autant que cela ne soit malheureusement [pas le cas pour tout le monde](http://blog.xero.com/2013/03/making-mobile-work/) ; tout dépendra donc du type d’usages auxquels vous destinez votre application.

## Le choix du framework Web mobile

Parmi l’offre pléthorique d’outils Open Source à disposition sur ce créneau en plein essor, nous avons évalué trois frameworks de développement Web mobile : **[iUI], [jQT] et [jquery-mobile]**.

### iUI

[iUI] est le moins complet et ne semble plus vraiment maintenu, il est néanmoins léger et très efficace pour un site basique. C’est par ailleurs le plus performant sur les animations de transition.

### jQT

[jQT] est un projet relativement actif, mais qui manque cruellement de documentation et nous a posé de nombreux problèmes quand à la gestion des évènements spécifiques à une utilisation mobile. De plus, il est très difficile d’étendre ou de hooker l’API proposée, ce qui s’est avéré rhédibitoire eu égard aux besoins du projet.

### jquery-mobile

[jquery-mobile] nous a finalement donné entière satisfaction, avec la possibilité de réaliser un thème [rapidement](http://jquerymobile.com/themeroller/), disposant d’une bonne extensibilité, la possibilité de débrayer tout ou partie des fonctionnalités de navigation intégrées (contrairement à jQT) et l’intégration native des fonctionnalités de *FastClick*.

Le catalogue de *widgets* est relativement complet, leur mise en place et leur configuration est rendue très aisée par l’utilisation des [data attributes] (même si l’on peut toutefois questionner la pertinence de les utiliser pour gérer la présentation par exemple…)

## *Appification* et contextes

Sur iOS, il est possible de placer un site — ou plutôt une URL — en tant que raccourci d’application sur l’écran d’accueil ; celui-ci peut alors disposer d’une icône dédiée et d’un écran d’attente de chargement au lancement, tout en masquant l’interface utilisateur de Safari.

Si cette solution nous semblait satisfaisante dans un premier temps, elle s’est vite révélée problématique lors des changements de contextes :

- l’ouverture d’un lien externe au sein de l’application ouvre inévitablement un nouvel *onglet* dans Safari ;
- la sortie vers un lecteur PDF ne permettant pas de retrouver l’application dans l’état où elle avait été quittée (ce qui est plutôt gênant pour un moteur de recherche)

Sous Android, la situation est à peine meilleure avec Chrome, puisqu’un clic sur un lien vers un document PDF entraîne son téléchargement en tâche de fond… Ne reste qu’une obscure notification une fois l’opération effectuée, nécessitant une action utilisateur pour le visionner.

Dans les deux cas, l’utilisateur lambda risque vraisemblablement d’être a minima perdu ou plus vraisembalement agacé par ces modes de fonctionnement.

**Au final, si certaines limites nous semblent justifiées, d’autres laissent à penser que les plateformes ont tout à gagner (environ [30%](http://www.washingtonpost.com/wp-dyn/content/article/2011/02/18/AR2011021807943.html) en fait) à encourager le développement d’applications natives en conservant de manière stratégique ces freins au développement d’applications Web.**

[iUI]: http://www.iui-js.org/
[jQT]: http://jqtjs.com/
[jquery-mobile]: http://jquerymobile.com/
[data attributes]: http://ejohn.org/blog/html-5-data-attributes/
[FastClick]: https://github.com/ftlabs/fastclick
