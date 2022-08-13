import 'package:animated_theme_switcher/animated_theme_switcher.dart';
import 'package:flutter/material.dart';
import 'package:user_profile_shared_preferences_example/model/user.dart';
import 'package:user_profile_shared_preferences_example/page/edit_profile_page.dart';
import 'package:user_profile_shared_preferences_example/utils/user_preferences.dart';
import 'package:user_profile_shared_preferences_example/widget/appbar_widget.dart';
import 'package:user_profile_shared_preferences_example/widget/button_widget.dart';
import 'package:user_profile_shared_preferences_example/widget/profile_widget.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';

class ProfilePage extends StatefulWidget {
  @override
  _ProfilePageState createState() => _ProfilePageState();
}

class _ProfilePageState extends State<ProfilePage> {
  @override
  Widget build(BuildContext context) {
    final user = UserPreferences.getUser();

    return ThemeSwitchingArea(
      child: Builder(
        builder: (context) => Scaffold(
          appBar: buildAppBar(context),
          body: ListView(
            physics: BouncingScrollPhysics(),
            children: [
              ProfileWidget(
                imagePath: user.imagePath,
                onClicked: () async {
                  await Navigator.of(context).push(
                    MaterialPageRoute(builder: (context) => EditProfilePage()),
                  );
                  setState(() {});
                },
              ),
              const SizedBox(height: 5),
              buildName(user),
              buildAbout(user),
              const SizedBox(
                height: 5,
              ),
              Center(child: buildUpgradeButton()),
              const SizedBox(height: 5),
              const SizedBox(
                height: 5,
              ),
              Center(child: buildUpgradeButton1()),
              const SizedBox(height: 5),
              const SizedBox(
                height: 5,
              ),
              Center(child: buildUpgradeButton2()),
              const SizedBox(height: 5),
              const SizedBox(
                height: 5,
              ),
              Center(child: buildUpgradeButton3()),
              const SizedBox(height: 5),
              const SizedBox(
                height: 5,
              ),
              Center(child: buildUpgradeButton4()),
              const SizedBox(height: 5),
            ],
          ),
        ),
      ),
    );
  }

  Widget buildName(User user) => Column(
        children: [
          Text(
            user.name,
            style: TextStyle(fontWeight: FontWeight.bold, fontSize: 24),
          ),
          const SizedBox(
            height: 4,
          ),
          Text(
            user.email,
            style: TextStyle(color: Colors.grey),
          )
        ],
      );

  Widget buildAbout(User user) => Container(
        padding: EdgeInsets.symmetric(horizontal: 48),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const SizedBox(height: 16),
            Text(
              user.about,
              style: TextStyle(fontSize: 16, height: 1.4),
            ),
          ],
        ),
      );
  Widget buildUpgradeButton() => Container(
        width: 300,
        child: ButtonWidget(
          text: ('Hesabım'),
          onClicked: () {},
        ),
      );
  @override
  Widget buildUpgradeButton1() => Container(
        width: 300,
        child: ButtonWidget(
          text: 'Bildirimler',
          onClicked: () {},
        ),
      );
  Widget buildUpgradeButton2() => Container(
        width: 300,
        child: ButtonWidget(
          text: 'Destek',
          onClicked: () {},
        ),
      );
  Widget buildUpgradeButton3() => Container(
        width: 300,
        decoration: BoxDecoration(),
        child: ButtonWidget(
          text: 'Çıkış',
          onClicked: () {},
        ),
      );
  Widget buildUpgradeButton4() => Container(
        width: 300,
        child: SizedBox(
          child: ButtonWidget(
            text: 'Bilgileri Güncelle',
            onClicked: () {},
          ),
        ),
      );
}
