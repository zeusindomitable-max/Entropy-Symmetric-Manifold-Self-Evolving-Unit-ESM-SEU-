from src.esm_seu import esm_stability_energy

def test_basic_energy():
    assert abs(esm_stability_energy(1.0, 0.5) - 1.0) < 1e-6
  
