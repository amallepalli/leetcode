public class MaxSubArray {
    public int maxSubsArray(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        int maxValue = maxSubs(nums, left, right);
        return maxValue;
    }
    public int maxSubs(int[] nums, int left, int right) {
        if (right - left <= 0) {
            return nums[right];
        }
        int mid = (left + right) / 2;
        int lms = maxSubs(nums, left, mid);
        int rms = maxSubs(nums, mid+1, right);
        int maxVal = maxCrossingSum(nums, left, mid, right);
        maxVal = Math.max(lms, Math.max(rms, maxVal));
        return maxVal;
    }
    private int maxCrossingSum(int[] nums, int left, int mid, int right) {
        int leftSum = Integer.MIN_VALUE;
        int sum = 0;
        for (int i = mid; i >= left; i--) { 
            sum += nums[i];
            leftSum = Math.max(leftSum, sum);
        }

        int rightSum = Integer.MIN_VALUE;
        sum = 0;
        for (int i = mid + 1; i <= right; i++) {
            sum += nums[i];
            rightSum = Math.max(rightSum, sum);
        }

        return leftSum + rightSum;
    }
}
