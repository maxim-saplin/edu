﻿namespace Sample
{
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Canon;
	open Microsoft.Quantum.Convert;

	// Setting value of the qubit to the desired value (Result)
	operation Set (desired: Result, q1: Qubit) : Unit
    {
		let current = M(q1); // measuring and collapsing the qubit and getting 0 or 1
		if (desired != current)
		{
			X(q1); // if not desired value, we invert via NOT
		}   
    }

	// Running 4 qubit calculation
	@EntryPoint()
	operation QB4Run () : Unit
    {
		// Counters measuring how many times the given qubit was 0
		// Naming, starting from rightm i.e. qubits #4321, 16 comb
		mutable num0000 = 0;
		mutable num0001 = 0;
		mutable num0010 = 0;
		mutable num0011 = 0;
		mutable num0100 = 0;
		mutable num0101 = 0;
		mutable num0110 = 0;
		mutable num0111 = 0;
		mutable num1000 = 0;
		mutable num1001 = 0;
		mutable num1010 = 0;
		mutable num1011 = 0;
		mutable num1100 = 0;
		mutable num1101 = 0;
		mutable num1110 = 0;
		mutable num1111 = 0;

		use qubits = Qubit[4] // using 4 qubits
		{
			// Unceoment corresponding section to see the results od qubit operation
			for test in 1..10000 // number of samples
			{
				// Init
				Set (Zero, qubits[0]);
				Set (Zero, qubits[1]);
				Set (Zero, qubits[2]);
				Set (Zero, qubits[3]);

				//Pass through (NOP)
				//Set (Zero, qubits[0]);
				//Set (Zero, qubits[1]);
				//Set (Zero, qubits[2]);
				//Set (Zero, qubits[3]);

				//NOT gate
				//Set (Zero, qubits[0]);
				//X(qubits[0]);

				//Hadamard - setting to superposition
				Set (Zero, qubits[0]);
				H(qubits[0]);
				// 0000 -> 0,5041
				// 0001 -> 0,4959
				// 0010 -> 0
				// 0011 -> 0
				// ...

				//SWAP
				//Set (One, qubits[0]);
				//SWAP (qubits[0],qubits[1]);

				//Controlled-NOT   ( CNOT )
				//Set (One, qubits[0]);
				//Set (Zero, qubits[1]);
				//CNOT(qubits[0],qubits[1]);

				//Bell State
				//Set (Zero, qubits[0]);
				//Set (Zero, qubits[1]);
				//H(qubits[0]);
				//CNOT(qubits[0],qubits[1]);

				//Toffoli Gate in general configuration
				//Set (One, qubits[0]);
				//Set (One, qubits[1]);
				//Set (One, qubits[2]);
				//CCNOT(qubits[0],qubits[1],qubits[2]);

				//Toffoli Gate in NOT configuration
				//Set (One, qubits[0]); // Always 1
				//Set (One, qubits[1]); // Always 1
				//Set (One, qubits[2]); // Input of NOT gate. Gets inverted by NOT
				//CCNOT(qubits[0],qubits[1],qubits[2]);

				//Toffoli Gate in AND configuration
				//Set (One, qubits[0]); // Input 1 of AND
				//Set (One, qubits[1]); // Input 2 of AND
				//Set (Zero, qubits[2]);// Initialized to 0. Gets the result of AND
				//CCNOT(qubits[0],qubits[1],qubits[2]);

				//Toffoli Gate in FANOUT configuration
				//Set (One, qubits[0]); // Always 1
				//Set (One, qubits[1]); // Input & Pass through.
				//Set (Zero, qubits[2]); //Initialized to 0. Gets a result of the fanout from qubits[1]
				//CCNOT(qubits[0],qubits[1],qubits[2]);


				// Measauring the output values
				let res0 = M (qubits[0]);
				let res1 = M (qubits[1]);
				let res2 = M (qubits[2]);
				let res3 = M (qubits[3]);

				if(res3 == Zero and res2 == Zero and res1 == Zero and res0 == Zero){set num0000 = num0000 + 1;}
				if(res3 == Zero and res2 == Zero and res1 == Zero and res0 == One ){set num0001 = num0001 + 1;}
				if(res3 == Zero and res2 == Zero and res1 == One  and res0 == Zero){set num0010 = num0010 + 1;}
				if(res3 == Zero and res2 == Zero and res1 == One  and res0 == One ){set num0011 = num0011 + 1;}
				if(res3 == Zero and res2 == One  and res1 == Zero and res0 == Zero){set num0100 = num0100 + 1;}
				if(res3 == Zero and res2 == One  and res1 == Zero and res0 == One ){set num0101 = num0101 + 1;}
				if(res3 == Zero and res2 == One  and res1 == One  and res0 == Zero){set num0110 = num0110 + 1;}
				if(res3 == Zero and res2 == One  and res1 == One  and res0 == One ){set num0111 = num0111 + 1;}
				if(res3 == One  and res2 == Zero and res1 == Zero and res0 == Zero){set num1000 = num1000 + 1;}
				if(res3 == One  and res2 == Zero and res1 == Zero and res0 == One ){set num1001 = num1001 + 1;}
				if(res3 == One  and res2 == Zero and res1 == One  and res0 == Zero){set num1010 = num1010 + 1;}
				if(res3 == One  and res2 == Zero and res1 == One  and res0 == One ){set num1011 = num1011 + 1;}
				if(res3 == One  and res2 == One  and res1 == Zero and res0 == Zero){set num1100 = num1100 + 1;}
				if(res3 == One  and res2 == One  and res1 == Zero and res0 == One ){set num1101 = num1101 + 1;}
				if(res3 == One  and res2 == One  and res1 == One  and res0 == Zero){set num1110 = num1110 + 1;}
				if(res3 == One  and res2 == One  and res1 == One  and res0 == One ){set num1111 = num1111 + 1;}
				
				
			}

			// Reseting qubits to 0 at the end of the operation as reqjuired by Q#

			Set(Zero, qubits[0]);
			Set(Zero, qubits[1]);
			Set(Zero, qubits[2]);
			Set(Zero, qubits[3]);
		}
		
		Message("0000 -> " + DoubleAsString(IntAsDouble(num0000)/10000.0));
		Message("0001 -> " + DoubleAsString(IntAsDouble(num0001)/10000.0));
		Message("0010 -> " + DoubleAsString(IntAsDouble(num0010)/10000.0));
		Message("0011 -> " + DoubleAsString(IntAsDouble(num0011)/10000.0));
		Message("0100 -> " + DoubleAsString(IntAsDouble(num0100)/10000.0));
		Message("0101 -> " + DoubleAsString(IntAsDouble(num0101)/10000.0));
		Message("0110 -> " + DoubleAsString(IntAsDouble(num0110)/10000.0));
		Message("0111 -> " + DoubleAsString(IntAsDouble(num0111)/10000.0));
		Message("1000 -> " + DoubleAsString(IntAsDouble(num1000)/10000.0));
		Message("1001 -> " + DoubleAsString(IntAsDouble(num1001)/10000.0));
		Message("1010 -> " + DoubleAsString(IntAsDouble(num1010)/10000.0));
		Message("1011 -> " + DoubleAsString(IntAsDouble(num1011)/10000.0));
		Message("1100 -> " + DoubleAsString(IntAsDouble(num1100)/10000.0));
		Message("1101 -> " + DoubleAsString(IntAsDouble(num1101)/10000.0));
		Message("1110 -> " + DoubleAsString(IntAsDouble(num1110)/10000.0));
		Message("1111 -> " + DoubleAsString(IntAsDouble(num1111)/10000.0));
    }
}
