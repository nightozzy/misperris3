var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
	'/registro/',
	'/static/core/css/estilos.css',
	'/static/core/css/registro.css',
	'/static/core/css/bootstrap.min.css',
	'/static/core/js/bootstrap.min.js',
	'/static/core/js/combo.js',
	'/static/core/js/validaciones.js',
	'/static/core/img/apolo.jpg',
	'/static/core/img/crowfunding.jpg',
	'/static/core/img/logo.png',
	'/static/core/img/perro.png',
	'/static/core/img/logo.png',
	'/static/core/img/perro.png',
	'/static/core/img/rescate.jpg',
	'/static/core/img/soc1.png',
	'/static/core/img/soc2.png',
	'/static/core/img/soc3.png',
	'/static/core/img/soc4.png',
	'/static/core/img/ul.gif',
	'https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.css',
	'https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js',
	'https://cdnjs.cloudflare.com/ajax/libs/fancybox/3.3.5/jquery.fancybox.min.css',
	'https://cdnjs.cloudflare.com/ajax/libs/fancybox/3.3.5/jquery.fancybox.min.js',
	'/static/core/img/adoptados/Apolo.jpg',
	'/static/core/img/adoptados/Duque.jpg',
	'/static/core/img/adoptados/Tom.jpg',
	'/static/core/img/rescatados/Bigotes.jpg',
	'/static/core/img/rescatados/Chocolate.jpg',
	'/static/core/img/rescatados/Luna.jpg',
	'/static/core/img/rescatados/Maya.jpg',
	'/static/core/img/rescatados/Oso.jpg',
	'/static/core/img/rescatados/Pexel.jpg',
	'/static/core/img/rescatados/Wifi.jpg',
	'/static/core/img/fondo.jpg',
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event){
    event.respondWith(
        caches.match(event.request).then(function(response) {
            if(response) {
                return response;
            }

            return fetch(event.request);
        })
    );
});

