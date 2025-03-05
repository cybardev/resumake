{ pkgs }:
pkgs.dockerTools.buildImage {
  name = "resumake";
  copyToRoot = pkgs.buildEnv {
    name = "image-root";
    paths = with pkgs; [
      python3Packages.weasyprint
      roboto
      (pkgs.callPackage ./resumake.nix { })
    ];
    pathsToLink = [
      "/bin"
      "/share"
    ];
  };
  config = {
    WorkingDir = "/app";
    Cmd = [
      "resumake"
      "-p"
      "80"
    ];
    ExposedPorts = {
      "80" = { };
    };
  };
}
