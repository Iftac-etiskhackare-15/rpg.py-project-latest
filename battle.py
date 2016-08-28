class Battle:
    playerHealth=0
    enemyDamage=0
    playerDamage=0
    enemyHealth=0
    def __init__(self, arg1, arg2, arg3, arg4):
        # constructor
        self.playerHealth=arg1
        self.enemyDamage=arg2
        self.playerDamage=arg3
        self.enemyHealth=arg4
    def fight_playerTakeDamage(self):
        self.playerHealth-=self.enemyDamage
        return self.playerHealth
    def fight_enemyTakeDamage(self):
        self.enemyHealth-=self.playerDamage
        return self.enemyHealth
