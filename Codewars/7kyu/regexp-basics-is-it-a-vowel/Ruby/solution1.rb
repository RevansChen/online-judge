# Ruby - MRI 2.5.0

class String
    def vowel?
        match(/\A[aeiou]\z/i) != nil
    end
end
