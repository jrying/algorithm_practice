public class Solution {
    public List<Integer> largestDivisibleSubset(int[] nums) {
        Arrays.sort(nums);
        List<Integer> longest = new ArrayList();
        List<List<Integer>> current = new ArrayList();
        for (int i = 0; i < nums.length; i++) {
            int index = -1, length = 0;
            for (int j = i - 1; j >= 0; j--) {
                if (nums[i] % nums[j] == 0 && current.get(j).size() > length) {
                    index = j;
                    length = current.get(j).size();
                }
            }
            List<Integer> list;
            if (index > -1) {
                list = new ArrayList(current.get(index));
            }
            else {
                list = new ArrayList();
            }
            list.add(nums[i]);
            current.add(list);
            if (list.size() > longest.size()) {
                longest = list;
            }
        }
        return longest;
    }
}
