from src.esm_core import EffectiveHamiltonian

def test_effective_hamiltonian():
    H = EffectiveHamiltonian(eta=2.0)
    result = H.compute(1.5)
    assert abs(result - 3.0) < 1e-8, "Effective Hamiltonian computation error."
