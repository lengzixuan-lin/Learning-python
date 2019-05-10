def main():
    persons = [x for x in range(1, 31)]
    dropped = 0
    while (dropped < 15):
        persons = persons[9:] + persons[0:8]
        dropped += 1
    print ('基督徒的原始位置为：')
    print (sorted(persons))
if __name__ == '__main__':
    main()
