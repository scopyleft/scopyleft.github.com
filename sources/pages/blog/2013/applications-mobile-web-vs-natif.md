title: "Développer une application web sur mobile"
date: 2013-03-14
published: false

Nous avons récemment eu à enrichir une application web d'intranet afin d'aménager un accès pour des utilisateurs de mobiles (parc de périphériques connu et contrôlé). Trois approches étaient possibles :

- l'utilisation d'un [*responsive design*](https://fr.wikipedia.org/wiki/Responsive_Web_Design) sur la version Web pour réutiliser l'existant mais cela posait des problèmes de performances (chargement inutile de l'intégralité du HTML et des ressources de la page, mise en cache complexe) ;
- l'utilisation de code natif — ou d'un intermédiaire comme [Titanium](http://www.appcelerator.com/platform/titanium-sdk/) — pour bénéficier de la réactivité et des APIs mais cela nous liait trop fortement aux plateformes propriétaires ;
- l'utilisation d'une version web dédiée aux périphériques à petits écrans, c'est celle pour laquelle nous avons opté en misant sur la pérennité et l'évolutivité d'une telle approche.

Rapidement, nous avons été confrontés à plusieurs problèmes que nous souhaitions partager avec vous :

## La réactivité

C'était la grande inconnue et nous avons rapidement opté pour une architecture permettant de servir les données en JSON via une API HTTP pour alimenter une application JavaScript en [Backbone.js](http://backbonejs.org/) avec la possibilité de mettre en cache les données côté client (utile lorsque la connexion est aléatoire !).

La latence perceptible au *tap* sur un périphérique iOS qui affiche une page web s'explique par Apple qui [semblent préconiser de patienter 300ms](http://cubiq.org/remove-onclick-delay-on-webkit-for-iphone) avant de prendre en compte l'action de l'utilisateur, cela nous semblait trop important compte-tenu de la cible et nous nous sommes tournés vers la bibliothèque [FastClick](https://github.com/ftlabs/fastclick) pour y pallier.

## Le choix du framework

Nous avons évalué les différentes solutions possibles dans le domaine pour en retenir 3 : [iUI](http://www.iui-js.org/), [jQTouch](http://jqtjs.com/) et [jquery-mobile](http://jquerymobile.com/).

Le premier est le moins complet et ne semblait plus vraiment maintenu, il est néanmoins très efficace pour un site basique. Le second est très actif mais manque de documentation et comportait des bugs relatifs au *tap* qui était considéré comme un *double tap* lors d'une utilisation conjointe à FastClick. De plus, la qualité du code laissait à désirer. Le troisième nous a finalement donné entière satisfaction avec la possibilité de réaliser un thème [rapidement](http://jquerymobile.com/themeroller/).

## *Appification* et contextes

Il est possible de placer des sites (ou plutôt des URLs) en écran d'accueil des périphériques iOS avec une icône et un écran d'attente de chargement au lancement tout en masquant l'interface utilisateur de Safari.

Si cette solution nous semblait satisfaisante dans un premier temps, elle s'est vite révélée être problématique lors des changements de contextes : l'ouverture d'un lien au sein de « l'application » renvoyant inévitablement sur Safari et la sortie vers un lecteur PDF ne permettant pas de retrouver l'application dans l'état où elle avait été quittée (ce qui est plutôt gênant pour un moteur de recherche).

**Au final, si certaines limites nous semblent justifiées, d'autres laissent à penser que les plateformes ont tout à gagner (environ [30%](http://www.washingtonpost.com/wp-dyn/content/article/2011/02/18/AR2011021807943.html) en fait) à encourager le développement d'applications natives en conservant de manière stratégique ces freins au développement d'applications web.**
