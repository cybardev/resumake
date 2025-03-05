{
  pkgs,
}:

let
  resumake = pkgs.callPackage ./resumake.nix;
in
pkgs.dockerTools.buildImage {
  name = "resumake";
  copyToRoot = pkgs.buildEnv {
    name = "image-root";
    paths = with pkgs; [
      python3Packages.weasyprint
      roboto
      resumake
    ];
    pathsToLink = [
      "/bin"
      "/share"
    ];
  };
  config = {
    Cmd = [
      "${resumake}/bin/resumake"
      "-p"
      80
    ];
    ExposedPorts = {
      "80" = { };
    };
  };
}
