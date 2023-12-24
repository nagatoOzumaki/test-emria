# Méthode Naive

def fiboncci(n):
    # Cas de base
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    else:
        # Appel récursif
        return fiboncci(n - 1) + fiboncci(n - 2)
    



# Méthode optimisée : Utilisation de la mémorisation pour optimiser le calcul de Fibonacci
memo = {}

def fibonacci_mem(n):
    # Cas de base
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Vérifier si la valeur est déjà mémorisée
    if n in memo:
        return memo[n]
    
    # Calculer et mémoriser le résultat
    result = fibonacci_mem(n - 1) + fibonacci_mem(n - 2)
    memo[n] = result
    
    return result

# Tester la fonction
print(fibonacci_mem(5))
print(fibonacci_mem(8))
print(fibonacci_mem(10))
