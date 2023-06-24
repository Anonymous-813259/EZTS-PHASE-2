families={
    'Charley' : {
        'Sam' : {'Boxy','Rosy'},
        'Nila' :{'Pepsi'}
    },
    'Devi' : {
        'Tommy' : {'Tony'},
        'Timmy' : {'Hamster'},
        'Tammy' : {'Hamster'}
    },
    'Carlos' : {
        'Diego' : 'Cat',
        'Ferret' : 'Fox'
    }
}

for parent,children in families.items():
    print(f"{parent} has {len(children)} kids:",end=' ')
    print(f"{', and '.join([str(Child) for Child in [*children]])}")