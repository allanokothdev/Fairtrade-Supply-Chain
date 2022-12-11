from pyteal import *

from supply_chain import Stage

if __name__ == "__main__":
    approval_program = Stage().approval_program()
    clear_program = Stage().clear_program()

    # Mode.Application specifies that this is a smart contract
    compiled_approval = compileTeal(
        approval_program, Mode.Application, version=5)
    print(compiled_approval)
    with open("supply_chain.teal", "w") as teal:
        teal.write(compiled_approval)
        teal.close()

    # Mode.Application specifies that this is a smart contract
    compiled_clear = compileTeal(clear_program, Mode.Application, version=5)
    print(compiled_clear)
    with open("supply_chain.teal", "w") as teal:
        teal.write(compiled_clear)
        teal.close()
