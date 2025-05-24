"""Entry point for the homework package."""

# python3 -m homework data/input data/output

from .src.main import main

if __name__ == "__main__":
    main()

# Con esto, creamos un paquete, entonces se llamaría:
# python3 -m homework --model elasticnet --l1_ratio 0.1 --alpha 1
