from LetterCombination import LetterCombinationSolution

def main():
    solution = LetterCombinationSolution()
    assert(solution.letterCombinations("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"] )
    assert(solution.letterCombinations("") == [] )
    assert(solution.letterCombinations("2") == ["a","b","c"] )
    assert(solution.letterCombinations("987") == ["wtp","wtq","wtr","wts","wup","wuq","wur","wus","wvp","wvq","wvr","wvs","xtp","xtq","xtr","xts","xup","xuq","xur","xus","xvp","xvq","xvr","xvs","ytp","ytq","ytr","yts","yup","yuq","yur","yus","yvp","yvq","yvr","yvs","ztp","ztq","ztr","zts","zup","zuq","zur","zus","zvp","zvq","zvr","zvs"] )

if __name__ == "__main__":
    main()