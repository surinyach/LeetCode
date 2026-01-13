class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total_gas = 0
        total_cost = 0
        for i in range(0, len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
        
        if total_cost > total_gas:
            return -1
        
        index = 0
        tank = 0
        for i in range(0, len(gas)):
            if tank < 0: 
                index = i
                tank = 0
            tank += gas[i]
            tank -= cost[i]
        return index