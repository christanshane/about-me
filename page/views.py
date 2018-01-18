from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    html = """
    {% load staticfiles %}
    <!DOCTYPE html>
    <html lang="en">
    
      <head>
    
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <meta name="description" content="">
        <meta name="author" content="">
    
        <title>Christan Shane D. Plaza | About Me</title>
    
        <!-- Bootstrap core CSS -->
        <link href="/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://getbootstrap.com/dist/css/bootstrap.min.css" rel="stylesheet">
    
        <!-- Custom fonts for this template -->
        <link href="https://fonts.googleapis.com/css?family=Catamaran:100,200,300,400,500,600,700,800,900" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css?family=Lato:100,100i,300,300i,400,400i,700,700i,900,900i" rel="stylesheet">
    
        <!-- Custom styles for this template -->
        <link href="/page/static/css/one-page-wonder.min.css" rel="stylesheet">
    
      </head>
    
      <body>
    
        <!-- Navigation -->
    <!--
        <nav class="navbar navbar-expand-lg navbar-dark navbar-custom fixed-top">
          <div class="container">
            <a class="navbar-brand" href="#">About Me</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarResponsive">
              <ul class="navbar-nav ml-auto">
                <li class="nav-item">
                  <a class="nav-link" href="#First">Sign Up</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#">Log In</a>
                </li>
              </ul>
            </div>
          </div>
        </nav>
    -->
    
        <header class="masthead text-center text-white">
            
            <br>
            <br>
            <br>
            <br>
          <div class="masthead-content">
            <div class="container">
              <h1 class="masthead-heading mb-0">Christan Shane D. Plaza</h1>
              <h2 class="masthead-subheading mb-0">A very useless Biography</h2>
              <a href="#First" class="btn btn-primary btn-xl rounded-pill mt-5">Learn More About Me</a>
            </div>
          </div>
          <div class="bg-circle-1 bg-circle"></div>
          <div class="bg-circle-2 bg-circle"></div>
          <div class="bg-circle-3 bg-circle"></div>
          <div class="bg-circle-4 bg-circle"></div>
        </header>
        
        <section id="First">
          <div class="container">
            <div class="row align-items-center">
              <div class="col-lg-6 order-lg-2">
                <div class="p-5">
                  <images class="images-fluid rounded-circle" src="https://i.imgur.com/W5rdBYD.jpg" alt="">
                </div>
              </div>
              <div class="col-lg-6 order-lg-1">
                <div class="p-5">
                  <h2 class="display-4">Your Typical Avid Gamer and Programmer</h2>
                  <p>Christan started programming at the age of 11. His parents has influenced him in playing games when he was as young as 4 years old.
                    </p>
                </div>
              </div>
            </div>
          </div>
        </section>
    
        <section>
          <div class="container">
            <div class="row align-items-center">
              <div class="col-lg-6">
                <div class="p-5">
                  <images class="images-fluid rounded-circle" src="https://i.imgur.com/es3xtbO.jpg" alt="">
                </div>
              </div>
              <div class="col-lg-6">
                <div class="p-5">
                  <h2 class="display-4">Adrenaline Junkie</h2>
                  <p>Christan loves adventure. Though most of his adventures aren't your typical camping/basejumping kind of adventures. Roughly composed of biking through Bacolod's dangerous streets at 3am just to
                      drink Milo in Libertad.
                    </p>
                </div>
              </div>
            </div>
          </div>
        </section>
    
        <section>
          <div class="container">
            <div class="row align-items-center">
              <div class="col-lg-6 order-lg-2">
                <div class="p-5">
                  <images class="images-fluid rounded-circle" src="https://i.imgur.com/1k8KDRb.png" alt="">
                </div>
              </div>
              <div class="col-lg-6 order-lg-1">
                <div class="p-5">
                  <h2 class="display-4">"I no de wei"</h2>
                  <p>Christan has a very weird sense of humor. Very updated and knoweldgeable in 'internet memes'</p>
                </div>
              </div>
            </div>
          </div>
        </section>
    
        <!-- Footer -->
        <footer class="py-5 bg-black">
          <div class="container">
            <p class="m-0 text-center text-white small">Copyright &copy; Christan Shane D. Plaza 2018   </p>
          </div>
          <!-- /.container -->
        </footer>
    
        <!-- Bootstrap core JavaScript -->
        <script src="vendor/jquery/jquery.min.js"></script>
        <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
    
      </body>
    
    </html>

    """
    return HttpResponse(html)