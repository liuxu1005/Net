Test Result:

Distance Vector:
	Testing Euclidean __main__.DVRouterNetwork with no broken links...
		A---B   C---D
		|   | / | / |
		E   F---G---H
		link costs = 1 on straight links, sqrt(2) on diagonal links
	...PASSED
	
	Testing non-Euclidean __main__.DVRouterNetwork with no broken links
		 A-7-B-1-E
		 |     / |
		 1  2/   9
		 | /     |
		 C-4-D-1-F
	...PASSED
	
	Testing __main__.DVRouterNetwork with one broken link
	Breaking F-G link in topology ('X' marks the spot!)
		A---B   C---D
		|   | / | / |
		E   F-X-G---H
		link costs = 1 on straight links, sqrt(2) on diagonal links
	...PASSED
	
	Testing __main__.DVRouterNetwork prior to changing costs and more failures
		A---B-4-C---D
		|   | /2X /2|
		E---F---G---H
		Costs: BC=4 DG=2 CF=2 CG broken; all other costs are 1
	...PASSED
	
	Testing __main__.DVRouterNetwork with changing costs and more failures
		Now breaking CF, CG, DG; changing BF<--15, CD <--13
	...PASSED
	Testing convergence time on a simple network:
		  Y
		 / \
		X---Z
		Costs: XY=4 YZ=1 ZX=12
	Convergence time after changing Cost(Z->X) to 2: 52
	...PASSED
	Reset to original network
	Convergence time after changing Cost(X->Y) to 14: 390
	...PASSED
	
	Testing __main__.DVRouterNetwork with two broken links (disconnected network)
	Breaking links F-C and F-G ('X' marks the spot!)
		A---B   C---D
		|   | X | / |
		E   F-X-G---H
		link costs = distance (1 or sqrt(2))
	...PASSED
	
	**************************************************
	Tests complete for DVRouterNetwork Task
	**************************************************
	
	One more thing...
	Testing a network path with very high cost
	A-----B--------------------------C-----D
	   1      self.INFINITY-2           1   
	Routing Tables: (format: src, (dst1, link1), (dst2, link2), ...)
		A, (B,B), (C,B), (D,None)
		B, (A,A), (C,C), (D,C)
		C, (A,B), (B,B), (D,D)
		D, (A,None), (B,C), (C,C)
	Route from A<-->D exists in topology but your protocol says it doesn't!
	Why did this happen?  Give your answer in the pset. 
	Because the cost is on the edge, which is 32.
	
Link State:

	Testing Euclidean __main__.LSRouterNetwork with no broken links...
		A---B   C---D
		|   | / | / |
		E   F---G---H
		link costs = 1 on straight links, sqrt(2) on diagonal links
	...PASSED
	
	Testing non-Euclidean __main__.LSRouterNetwork with no broken links
		 A-7-B-1-E
		 |     / |
		 1  2/   9
		 | /     |
		 C-4-D-1-F
	...PASSED
	
	Testing __main__.LSRouterNetwork with one broken link
	Breaking F-G link in topology ('X' marks the spot!)
		A---B   C---D
		|   | / | / |
		E   F-X-G---H
		link costs = 1 on straight links, sqrt(2) on diagonal links
	...PASSED
	
	Testing __main__.LSRouterNetwork prior to changing costs and more failures
		A---B-4-C---D
		|   | /2X /2|
		E---F---G---H
		Costs: BC=4 DG=2 CF=2 CG broken; all other costs are 1
	...PASSED
	
	Testing __main__.LSRouterNetwork with changing costs and more failures
		Now breaking CF, CG, DG; changing BF<--15, CD <--13
	...PASSED
	Testing convergence time on a simple network:
		  Y
		 / \
		X---Z
		Costs: XY=4 YZ=1 ZX=12
	Convergence time after changing Cost(Z->X) to 2: 75
	...PASSED
	Reset to original network
	Convergence time after changing Cost(X->Y) to 14: 40
	...PASSED
	
	Testing __main__.LSRouterNetwork with two broken links (disconnected network)
	Breaking links F-C and F-G ('X' marks the spot!)
		A---B   C---D
		|   | X | / |
		E   F-X-G---H
		link costs = distance (1 or sqrt(2))
	...PASSED
	
	**************************************************
	Tests complete for LSRouterNetwork Task
	**************************************************
