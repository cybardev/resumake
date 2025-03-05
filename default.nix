let
  nixpkgs = fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-24.11";
  pkgs = import nixpkgs {
    config = { };
    overlays = [ ];
  };
in
{
  resumake = pkgs.callPackage ./resumake.nix { };
  dockerfile = pkgs.callPackage ./Dockerfile.nix { };
}
