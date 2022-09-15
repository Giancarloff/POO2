#include <iostream>
using namespace std;

float percentual(int v, int t) {
    return (float) v/t;
}

int main() {
    
    string newln = "\n";
    
    int voto = -1;
    int i = 0;
    int *array = new int[23];
    
    cout << "Digite os votos, 0 para sair" << newln;
    
    for (int j = 0; j < 24; j++) {
        array[j] = 0;
    }
    
    while (voto != 0) {
        cin >> voto;
        
        if (0 < voto && voto < 24) {
            i += 1;
            array[voto-1] += 1;
        } else if (voto != 0) {
            cout << "Voto inválido!" << newln;
        } else {
            cout << "Encerrado!" << newln;
        }
        
    }
    
    cout << "Votos computados: " << i << newln;
    
    int maior = 0;
    int imaior = 0;
    cout << "Jogador    Votos     %" << newln;
    for (int k = 0; k < 24; k++) {
        if (array[k] > 0) {
            cout << k+1 << "            " << array[k] << "      " << percentual(array[k], i)*100 << newln;
        }
        if (maior < array[k]) {
            maior = array[k];
            imaior = k;
        }
    }
    
    cout << "O melhor jogador foi o número " << imaior << ", com " << array[imaior] << " votos, correspondendo a " << percentual(array[imaior], i)*100 << "% do total de votos." << newln;
    return 0;
}