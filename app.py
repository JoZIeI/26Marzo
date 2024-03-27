from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_geek():
  return '''<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
<section style="background-color: #eee;">
    <div class="container py-5">
      <div class="row">
      </div>
      <div class="row">
        <div class="col-lg-4">
          <div class="card mb-4">
            <div class="card-body text-center">
              <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava3.webp" alt="avatar"
                class="rounded-circle img-fluid" style="width: 150px;">
              <h5 class="my-3">Jose Luis Taype Torrees</h5>
              <p class="text-muted mb-1">Estudiante</p>
              <p class="text-muted mb-4">Insitituto Continental</p>
            </div>
          </div>
        </div>
        <div class="col-lg-8">
          <div class="card mb-4">
            <div class="card-body">
              <div class="row">
                <div class="col-sm-3">
                  <p class="mb-0">Nombre Completo</p>
                </div>
                <div class="col-sm-9">
                  <p class="text-muted mb-0">Jose Luis</p>
                </div>
              </div>
              <hr>
              <div class="row">
                <div class="col-sm-3">
                  <p class="mb-0">Email</p>
                </div>
                <div class="col-sm-9">
                  <p class="text-muted mb-0">i2211258@continental.edu.pe</p>
                </div>
              </div>
              <hr>
              <div class="row">
                <div class="col-sm-3">
                  <p class="mb-0">Telefono</p>
                </div>
                <div class="col-sm-9">
                  <p class="text-muted mb-0">999999999</p>
                </div>
              </div>
              <hr>
            </div>
          </div>

        </div>
      </div>
    </div>
  </section><script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>'''


if __name__ == '__main__':
  app.run(host='0.0.0.0')
