import sys 

print("Lets get this done however shit this is")
sys.path.append("/Users/sanjukta/Documents/GitHub/approximate-circuit-compilation/")


from region_graph.algorithms.compiledrg import CompiledTree 
from symbolic.symbolic_circuit import SymbolicTensorizedCircuit
from layers import CPLayer, CategoricalLayer
from utils.type_aliases import SymbLayerCfg
from models.tensorized_circuit import TensorizedCircuit

cgraph = CompiledTree({'A', 'B', 'C', 'D'})
factorgraph = cgraph.topological_layers(bottom_up=True)

for eachgraph in factorgraph: 
    for eachlayer in eachgraph: 
        for eachnode in eachlayer:
            print(eachnode)

sym_circuit = SymbolicTensorizedCircuit(
    cgraph, 
    num_input_units= 4,
    num_sum_units= 4,
    input_cfg= SymbLayerCfg(layer_cls= CategoricalLayer), 
    sum_cfg= SymbLayerCfg(layer_cls=CPLayer),
    prod_cfg=SymbLayerCfg(layer_cls=CPLayer))


pc = TensorizedCircuit(sym_circuit)
print(pc)