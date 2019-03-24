// JavaScript - Node v8.1.3

Test.assertSimilar(aspectRatio(640, 480), [854, 480]);
Test.assertSimilar(aspectRatio(960, 720), [1280, 720]);
Test.assertSimilar(aspectRatio(1440, 1080), [1920, 1080]);
Test.assertSimilar(aspectRatio(1920, 1440), [2560, 1440]);
