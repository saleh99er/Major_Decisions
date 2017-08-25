
def dorm_checker(checker):
    checker = str(checker)
    valid_input = False
    counter = 0
    A = ['mews','mews hall']
    B = ['townhouse','townhouse community']
    C = ['balch','balch hall']
    D = ['clara dickson','clara dickson hall']
    E = ['bauer','court-kay-bauer','court kay bauer','court-kay-bauer hall','court kay bauer hall']
    F = ['high rise','high rise','high rise #5','high rise #5']
    G = ['jameson','jameson hall']
    H = ['low rise','low rise','low-rise #6','low-rise #6','low rise #6','low rise #6','low-rise #6','low-rise #6']
    I = ['low-rise #7','low-rise #7','low rise #7','low rise #7','low-rise #7','low-rise #7']
    J = ['mary donlon','mary donlon hall','mary','mary hall','donlon','donolon hall', 'egg']
    K = ['akwe:kon','akwekon','akwe kon','akwe-kon']
    L = ['ecology house','ecology-house','center','the holland international living center', 'hilc', 'the hilc']
    N = ['just about music','the ecology-house','the ecology house']
    M = ['holland international living jam']
    O = ['latino living center','the latino living center','llc']
    P = ['multicultural living learning unit','multicultural living learning unit','the multicultural living learning unit','mcllu']
    Q = ['risley residential college','the risley residential college','risley']
    R = ['ujamaa residential college','uj','ujamaa','the ujamaa residential college']
    S = ['language house','the language house','lh']
    master_dorm_list=[A,B,C,D,E,G,H,I,J,K,L,M,N,O,P,Q,R,S]
    for list_value in master_dorm_list:
        if checker in list_value:
            counter = counter + 1
        if counter == 1:
            valid_input = True
    return valid_input
            #print "valid input is" + str(valid_input)
                
    
                