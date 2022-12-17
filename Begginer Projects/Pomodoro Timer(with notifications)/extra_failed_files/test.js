var notifLib = Microsoft.Toolkit.Uwp.Notifications;

var toastContent = new notifLib.ToastContent();
var toastVisual = new notifLib.ToastVisual();
var toastBindingGeneric = new notifLib.ToastBindingGeneric();
var toastGenericHeroImage = new notifLib.ToastGenericHeroImage();
toastGenericHeroImage.source = "Assets/Apps/Food/Food1.jpg";
toastBindingGeneric.heroImage = toastGenericHeroImage;


var adaptiveText = new notifLib.AdaptiveText();
adaptiveText.text = "New suggested restaurant";
adaptiveText.hintMaxLines = 1;
toastBindingGeneric.children.push(adaptiveText);

adaptiveText = new notifLib.AdaptiveText();
adaptiveText.text = "There's a popular chinese restaurant near you that we think you'd like!";
toastBindingGeneric.children.push(adaptiveText);

var adaptiveImage = new notifLib.AdaptiveImage();
adaptiveImage.source = "Assets/Apps/Food/RestaurantMap.jpg";
toastBindingGeneric.children.push(adaptiveImage);

var adaptiveGroup = new notifLib.AdaptiveGroup();

var adaptiveSubgroup = new notifLib.AdaptiveSubgroup();

adaptiveText = new notifLib.AdaptiveText();
adaptiveText.text = "Pho Licious";
adaptiveText.hintStyle = notifLib.AdaptiveTextStyle.body;
adaptiveSubgroup.children.push(adaptiveText);

adaptiveText = new notifLib.AdaptiveText();
adaptiveText.text = "4.6 stars";
adaptiveText.hintStyle = notifLib.AdaptiveTextStyle.captionSubtle;
adaptiveSubgroup.children.push(adaptiveText);

adaptiveGroup.children.push(adaptiveSubgroup);

adaptiveSubgroup = new notifLib.AdaptiveSubgroup();

adaptiveText = new notifLib.AdaptiveText();
adaptiveText.text = "4018 148th Ave NE, Redmond, WA 98052";
adaptiveText.hintStyle = notifLib.AdaptiveTextStyle.captionSubtle;
adaptiveText.hintWrap = true;
adaptiveText.hintAlign = notifLib.AdaptiveTextAlign.right;
adaptiveSubgroup.children.push(adaptiveText);

adaptiveSubgroup.hintTextStacking = notifLib.AdaptiveSubgroupTextStacking.bottom;
adaptiveGroup.children.push(adaptiveSubgroup);

toastBindingGeneric.children.push(adaptiveGroup);

toastVisual.bindingGeneric = toastBindingGeneric;

toastContent.visual = toastVisual;

var toastActionsCustom = new notifLib.ToastActionsCustom();

var toastButton = new notifLib.ToastButton("Map", "bingmaps:?q=4018 148th Ave NE, Redmond, WA 98052");
toastButton.activationType = notifLib.ToastActivationType.protocol;
toastActionsCustom.buttons.push(toastButton);

toastButton = new notifLib.ToastButton("Reviews", "action=viewRestaurantReviews&restaurantId=92187");
toastButton.activationType = notifLib.ToastActivationType.foreground;
toastActionsCustom.buttons.push(toastButton);

toastContent.actions = toastActionsCustom;

toastContent.launch = "action=viewRestaurant&restaurantId=92187";

// Create the toast notification
var toastNotif = new Windows.UI.Notifications.ToastNotification(toastContent.getXml());

// And send the notification
Windows.UI.Notifications.ToastNotificationManager.createToastNotifier().show(toastNotif);