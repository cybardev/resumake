{
  lib,
  pkgs,
  buildGoModule,
  fetchFromGitHub,
}:

let
  author = "cybardev";
  pname = "resumake";
  version = "4.0.2";
in
buildGoModule {
  inherit pname;
  inherit version;

  src = fetchFromGitHub {
    owner = author;
    repo = pname;
    rev = "v${version}";
    hash = "sha256-UYKvjUJicgGAHzza7GYyLnlYfF6fK7aLL2VcLaA2L/I=";
  };

  nativeBuildInputs = [ pkgs.makeWrapper ];

  vendorHash = "sha256-qAcGgtnyPVXg3TPcjsrbQJqTOpqGwN4rftM6xUXy9+A=";

  ldflags = [
    "-s"
    "-w"
  ];

  postFixup = with pkgs; ''
    wrapProgram $out/bin/${pname} \
      --prefix PATH : ${
        lib.makeBinPath [
          python3Packages.weasyprint
          roboto
        ]
      }
  '';

  meta = {
    description = "Generate resume using data representation objects";
    homepage = "https://github.com/${author}/${pname}";
    license = lib.licenses.gpl3Only;
    mainProgram = pname;
    platforms = lib.platforms.all;
  };
}
