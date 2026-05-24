const standards = {
  "100free": {
    A: "58.50",
    AA: "55.00",
    AAA: "52.00"
  },
  "200free": {
    A: "2:10.00",
    AA: "2:02.00",
    AAA: "1:55.00"
  }
};

const swimmers = [
  {
    id: "SWCAN001",
    name: "Arthur Pigeon",
    year: 2011,
    club: "RL",
    bestTimes: {
      "100free": "56.21",
      "200free": "2:05.10"
    },
    meets: [
      {
        name: "Regional Champs",
        date: "2025-03-12",
        events: [
          { event: "100 Free", time: "56.21", rank: 3 },
          { event: "200 Free", time: "2:05.10", rank: 5 }
        ]
      }
    ]
  }
];
