public class HouseRobber {
    public int rob(int[] nums) {
        int[] dp = new int[nums.length];
        if (nums.length == 3) {
            return Math.max(nums[0] + nums[2], nums[1]);
        }
        else if (nums.length == 2) {
            return Math.max(nums[0], nums[1]);
        }
        else if (nums.length == 1) {
            return nums[0];
        }
        else {
            dp[0] = nums[0];
            dp[1] = nums[1];
            dp[2] = nums[2] + nums[0];
            for (int i = 3; i < nums.length; i++) {
                dp[i] = Math.max(nums[i] + dp[i-2], Math.max(nums[i] + dp[i-3], dp[i-1]));
            }
        }
        
        return dp[nums.length - 1];
    }
}
