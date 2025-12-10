# flake.nix
{
  description = "Advent of code";

  # Inputs are dependencies of your flake, like the nixpkgs repository
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  # Outputs are the things your flake provides
  outputs = {
    self,
    nixpkgs,
  }: let
    # This helper function makes your flake work on multiple systems (Linux, macOS, etc.)
    forAllSystems = nixpkgs.lib.genAttrs [
      "x86_64-linux"
      "aarch64-linux"
      "x86_64-darwin"
      "aarch64-darwin"
    ];

    # A function to get the nixpkgs package set for a given system
    pkgsFor = system: import nixpkgs {inherit system;};
  in {
    # We define a development shell
    devShells = forAllSystems (system: let
      pkgs = pkgsFor system;
    in {
      # The default development shell
      default = pkgs.mkShell {
        # The packages available in the shell
        packages = with pkgs; [
          python3
          python3Packages.numpy
          python3Packages.scipy
          python3Packages.tqdm
          python3Packages.pillow
        ];
      };
    });
  };
}
