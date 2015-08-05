mock_data.json:
Load this fixture when you need consistant data for dumping new file-based mock resources into the mdot client app. Update this fixture with:

./manage.py dumpdata --indent=4 mdot_rest.UWResource mdot_rest.IntendedAudience mdot_rest.ResourceLink
