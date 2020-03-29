import { NbMenuItem } from '@nebular/theme';

export const MENU_ITEMS: NbMenuItem[] = [
  {
    title: 'IoT Dashboard',
    icon: 'home-outline',
    link: '/pages/iot-dashboard',
  },
  {
    title: 'NLP',
    icon: 'map-outline',
    children: [
      {
        title: 'Sentiment Analysis-TextBlob',
        link: '/pages/nlp/textblob',
      }
    ],
  },
];
