def isPalindrome(self, s: str) -> bool:
        extract = ""
        for char in s:
            if (char.isalnum() == False):
                continue
            extract += char.lower()
        if (len(extract) == 0):
            return True
        i = 0
        j = len(extract) - 1
        while i < j:
            if (extract[i] != extract[j]):
                return False
            i += 1
            j -= 1
        return True