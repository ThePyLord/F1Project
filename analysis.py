from models import Circuits
import pandas as pd


def get_circuit_info(circuit_id):
    circuit = Circuits.Circuits.query.filter_by(circuit_id=circuit_id).first()
    return circuit

