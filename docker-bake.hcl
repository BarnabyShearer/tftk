arget "docker-metadata-action" {
  context = "./"
  platforms = [
    "linux/amd64",
    "linux/arm64"
  ]
}

group "default" {
  targets = ["python", "latest", "alpine", "debian", "dockerfromscratch", "python-alpine", "python-slim"]
}

target "python" {
  inherits = ["docker-metadata-action"]
  target = "python"
}

target "latest" {
  inherits = ["docker-metadata-action"]
  target = "latest"
}

target "alpine" {
  inherits = ["docker-metadata-action"]
  target = "alpine"
}

target "debian" {
  inherits = ["docker-metadata-action"]
  target = "debian"
}

target "dockerfromscratch" {
  inherits = ["docker-metadata-action"]
  target = "dockerfromscratch"
}

target "python-alpine" {
  inherits = ["docker-metadata-action"]
  target = "python-alpine"
}

target "python-slim" {
  inherits = ["docker-metadata-action"]
  target = "python-slim"
}

